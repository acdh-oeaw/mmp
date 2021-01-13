import glob
import json

from sqlalchemy import create_engine

from django.core.serializers.json import DjangoJSONEncoder

from django.apps import apps
from django.conf import settings
from django.core.exceptions import FieldDoesNotExist

from pandas import pandas as pd
from acdh_geonames_utils import acdh_geonames_utils as gn

from . populate_fields import *


dbc = settings.LEGACY_DB_CONNECTION
db_connection_str = f"mysql+pymysql://{dbc['USER']}:{dbc['PASSWORD']}@{dbc['HOST']}/{dbc['NAME']}"
db_connection = create_engine(db_connection_str)


def field_mapping(some_class):
    """ returns a dictionary mapping model field names to lookukp values
        :param some_class: Any django model class with extra field properties
        :return: A dict mapping model field names to lookukp values
    """
    field_mapping_dict = {}
    for x in some_class._meta.get_fields():
        try:
            field_mapping_dict[(x.extra['data_lookup']).lower().strip()] = x.name
        except:
            pass
    return field_mapping_dict


def field_mapping_inverse(some_class):
    """ returns a dictionary mapping model field names to lookukp values
        :param some_class: Any django model class with extra field properties
        :return: A dict mapping model field names to lookukp values
    """
    field_mapping_dict = {}
    for x in some_class._meta.get_fields():
        try:
            field_mapping_dict[x.name] = x.extra['data_lookup'].lower().strip()
        except:
            pass
    return field_mapping_dict


def fetch_models(app_name):
    """ returns all models from an app
        :param app_name: The name of the application you'd like to recieve the models from
        :return: A list of the app's model classes {app}.models.{ModelName}
    """
    all_models = [x for x in apps.all_models[app_name].values() if '_' not in x.__name__]
    return all_models


def create_file_class_map(app_name, format_string, glob_pattern):
    """ create a dictionary mapping model names to their spreadsheets
        (the spreadsheet must contain the model name)
        :param app_name: The name of the app you'd like to work with
        :format string: A python format string with one placeholder for the actual class name
        :glob_pattern: A python glob pattern matching the files you'd like to import data from
        :return: A dict where class names are keys and the full path to their matching files
    """
    all_models = fetch_models(app_name)
    files = glob.glob(glob_pattern)
    file_class_map = {}
    for cl in all_models:
        for file in files:
            con_file_name = format_string.format(cl.__name__).lower()
            if con_file_name in file.lower():
                file_class_map[cl.__name__] = file
    return file_class_map


def get_class_sources_map(app_name):
    """ create a dictionary mapping model names to their data source tables
        :param app_name: The name of the app you'd like to work with
        :return: A dict where class names are keys and the full path to their matching source tables
    """
    file_class_map = {}
    for x in fetch_models(app_name):
        if x.get_source_table() is not None:
            file_class_map[x.__name__] = x.get_source_table()
    return file_class_map


def run_import(
    app_name, m2m_sep="|", date_range_sep="/", limit=False,
    file_class_map_dict=False, filter_query=False, data_source='SQL'
):
    """ runs data import from a collection of excel-files matching the model class of the
        passed in applications
        :param app_name: name of the application
        :param m2m_sep: Character used in your data to separate values in a cell, defaults to '|'
        :param date_range_sep: Character used in your data to separate date ranges in a cell,
        defaults to '|'
        :param limit: The number of rows which should be imported, defaults to 'False', meaning all
        rows of each spreadsheet will be imported.
        :return: prints the name of the spraedsheet which is currently imported
        the populated database
    """
    if file_class_map_dict:
        file_class_map = file_class_map_dict
    else:
        print("new file class created")
        file_class_map = get_class_sources_map(app_name)
        print(file_class_map)
    for current_class in fetch_models(app_name):
        model_name = current_class.__name__
        print(model_name)
        try:
            source_name = file_class_map[current_class.__name__]
        except KeyError:
            print(f"no match for {model_name}")
            continue
        field_mapping_dict = field_mapping(current_class)
        print(field_mapping_dict)
        field_mapping_inverse_dict = field_mapping_inverse(current_class)
        if data_source == 'SQL':
            query = f"SELECT * FROM {source_name}"
            if filter_query:
                query = f"{query} {filter_query}"
            try:
                df_data = pd.read_sql(query, con=db_connection)
                print(source_name)
            except Exception as e:
                df_data = False
                print(source_name, e)
                continue
        elif data_source == 'GN':
            df_data = gn.donwload_to_df('AL')
            print("goood")
        else:
            df_data = False
        if isinstance(df_data, pd.DataFrame):
            df_data.columns = map(str.lower, df_data.columns)
            df_keys = df_data.keys()
            nr_cols = len(df_keys)
            legacy_id_field = current_class.get_natural_primary_key()
            legacy_id_source_field = field_mapping_inverse_dict[legacy_id_field]
            if limit:
                df_data = df_data.head(limit)
            for i, row in df_data.iterrows():
                try:
                    temp_item, _ = current_class.objects.get_or_create(
                        legacy_id=f"{float(row[legacy_id_source_field])}".lower().strip()
                    )
                except ValueError:
                    temp_item, _ = current_class.objects.get_or_create(
                        legacy_id=f"{row[legacy_id_source_field]}".strip()
                    )
                row_data = f"{json.dumps(row.to_dict(), cls=DjangoJSONEncoder)}"
                temp_item.orig_data_csv = row_data
                col_counter = 0
                while col_counter < nr_cols:
                    cur_attr = field_mapping_dict.get(df_keys[col_counter], df_keys[col_counter])
                    source_attr_name = df_keys[col_counter]
                    try:
                        cur_attr_type = current_class._meta.get_field(
                            cur_attr
                        ).get_internal_type()
                    except FieldDoesNotExist:
                        print(f"Field: {cur_attr} does not exist")
                        cur_attr_type = None
                    if cur_attr_type is not None:
                        # print("{}".format(cur_attr_type))
                        if "{}".format(cur_attr_type) == "CharField":
                            pop_char_field(
                                temp_item, row, cur_attr, max_length=249, fd=field_mapping_inverse_dict
                            )

                        elif "{}".format(cur_attr_type) == "TextField" and isinstance(
                            row[source_attr_name], str
                        ):
                            pop_text_field(temp_item, row, cur_attr, fd=field_mapping_inverse_dict)

                        elif "{}".format(cur_attr_type) == "IntegerField":
                            pop_int_field(temp_item, row, cur_attr, fd=field_mapping_inverse_dict)
                        
                        elif "{}".format(cur_attr_type) == "FloatField":
                            pop_float_field(temp_item, row, cur_attr, fd=field_mapping_inverse_dict)

                        elif "{}".format(cur_attr_type) == "ForeignKey" and isinstance(
                            f"{row[source_attr_name]}", str
                        ):
                            pop_fk_field(
                                current_class, temp_item,
                                row, cur_attr, fd=field_mapping_inverse_dict,
                                source_name=source_name
                            )
                        elif "{}".format(cur_attr_type) == "ManyToManyField" and isinstance(
                            row[source_attr_name], str
                        ):
                            pop_m2m_field(
                                current_class, temp_item, row, cur_attr,
                                sep=m2m_sep, fd=field_mapping_inverse_dict,
                                source_name=source_name
                            )

                        elif "{}".format(cur_attr_type) == "DateField":
                            pop_date_field(temp_item, row, cur_attr, fd=field_mapping_inverse_dict)

                        elif "{}".format(cur_attr_type) == "DateRangeField":
                            pop_date_range_field(
                                temp_item,
                                row,
                                cur_attr,
                                sep=date_range_sep,
                                fd=field_mapping_inverse_dict
                            )
                        else:
                            pass
                    # else:
                    #     print(f"cur: {cur_attr}, source: {source_attr_name}")
                    try:
                        temp_item.save()
                    except Exception as e:
                        print(e)
                    col_counter += 1


def delete_all(app_name):
    """ deletes all objects from passed in app
        :param app_name: the app to delte all model class objects from
    """
    print(app_name)
    all_models = fetch_models(app_name)
    print(all_models)
    for x in all_models:
        for y in x.objects.all():
            y.delete()


def import_m2m_tables(app_name, m2m_df, db_connection):
    """
        links objects listed in typical m2m tables
        :param app_name: the name of the app
        :param m2m_df: A dataframe derived from the gsheet-datamodel
        :param db_connection: A sqlalchemy create_engine object
        :returns: Acutally nothing, just populates the database.
    """

    model_dict = {x.__name__: x for x in fetch_models(app_name)}
    classes = m2m_df.groupby('class name technical')
    for x in classes:
        local_df = x[1].fillna(False)
        class_name = x[0]
        curr_class = model_dict[class_name]
        print(f"###########{curr_class}########")
        for i, row in local_df.iterrows():

            if row['value from']:
                source = row['value from']
            else:
                continue

            if '#' in source:
                continue
            cur_model_attr = row['field name technical']
            table, prop_1, prop_2 =  source.split('___')
            print(f"cur_model_attr: {cur_model_attr}; table: {table}; prop 1: {prop_1}")
            query = f"SELECT * FROM {table}"
            data_source = pd.read_sql(query, con=db_connection).dropna()
            for ds_i, ds_row in data_source.dropna().iterrows():
                legacy_id_source = f"{float(ds_row[prop_1])}"
                try:
                    curr_source = curr_class.objects.get(legacy_id=legacy_id_source)
                except Exception as e:
                    curr_source = None
                if curr_source is not None:
                    legacy_id_target = f"{float(ds_row[prop_2])}"
                    fk = curr_class._meta.get_field(cur_model_attr)
                    rel_model_name = fk.related_model._meta.model_name
                    if rel_model_name == 'skosconcept':
                        legacy_id_source = f"{cur_model_attr}__{legacy_id_target}".strip().lower()
                    else:
                        legacy_id_source = legacy_id_target
                    try:
                        curr_target = fk.related_model.objects.get(
                            legacy_id=legacy_id_source
                        )
                    except:
                        curr_target = None
                    if curr_source is not None and curr_target is not None:
                        m2m_attr = getattr(curr_source, cur_model_attr)
                        m2m_attr.add(curr_target)


def import_and_create_m2m(app_name, m2m_df, db_connection):
    """
        creates and links new objects with existing ones
        :param app_name: the name of the app
        :param m2m_df: A dataframe derived from the gsheet-datamodel
        :param db_connection: A sqlalchemy create_engine object
        :returns: Acutally nothing, just populates the database.
    """

    model_dict = {x.__name__: x for x in fetch_models(app_name)}
    classes = m2m_df.groupby('class name technical')
    for x in classes:
        local_df = x[1].fillna(False)
        class_name = x[0]
        curr_class = model_dict[class_name]
        print(f"###########{curr_class}########")
        for i, row in local_df.iterrows():

            if row['value from']:
                source = row['value from']
            else:
                continue
            cur_model_attr = row['field name technical']
            table, prop_1, prop_2 =  source.split('___')

            if '#' in source:
                prop_2, source_natural_pk = prop_2.split('#')
            else:
                source_natural_pk = None
            print(f"cur_model_attr: {cur_model_attr}; table: {table}; prop 1: {prop_1}, source_natural_pk: {source_natural_pk}")
            if '#' in source:
                query = f"SELECT * FROM {table}"
                data_source = pd.read_sql(query, con=db_connection).dropna()
                for ds_i, ds_row in data_source.dropna().iterrows():
                    legacy_id_source = f"{float(ds_row[prop_1])}"
                    try:
                        curr_source = curr_class.objects.get(legacy_id=legacy_id_source)
                    except Exception as e:
                        curr_source = None
                    if curr_source is not None:
                        if source_natural_pk is not None:
                            legacy_id_target = f"{(ds_row[prop_2])}"
    #                         print(legacy_id_target)
                        else:
                            pass
                            legacy_id_target = f"{float(ds_row[prop_2])}"
                        fk = curr_class._meta.get_field(cur_model_attr)
                        rel_model_name = fk.related_model._meta.model_name
                        if source_natural_pk is not None:
                            if rel_model_name == 'skosconcept':
                                scheme, _ = SkosConceptScheme.objects.get_or_create(
                                    dc_title=f"{cur_model_attr}"
                                )
                                skos_col, _ = SkosCollection.objects.get_or_create(
                                    name=f"{cur_model_attr}"
                                )
                                curr_target, _ = fk.related_model.objects.get_or_create(
                                        legacy_id=legacy_id_target[:249]
                                    )
                                curr_target.pref_label = legacy_id_target
                                curr_target.scheme.add(scheme)
                                curr_target.collection.add(skos_col)
                                curr_target.save()
                            else:
                                curr_target, _ = fk.related_model.objects.get_or_create(
                                        legacy_id=legacy_id_target[:249]
                                    )
                                setattr(curr_target, source_natural_pk, legacy_id_target)
                                try:
                                    curr_target.save()
                                except Exception as e:
                                    setattr(curr_target, source_natural_pk, legacy_id_target[:249])
                                    curr_target.save()
                            if curr_source is not None and curr_target is not None:
                                m2m_attr = getattr(curr_source, cur_model_attr)
                                m2m_attr.add(curr_target)
