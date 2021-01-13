import ast
import pandas as pd
import requests

from io import BytesIO

from jinja2 import Template

from django.apps import apps

from . import code_templates


GDRIVE_BASE_URL = "https://docs.google.com/spreadsheet/ccc?key="


def model_fields_to_dict(sample):
    """
    returns a list of dictionary fields from a given model
    :param sample: a model class
    """
    model_fields = []
    for x in sample._meta.get_fields():
        field_dict = {}
        if 'reverse_related' in f"{type(x)}":
            continue
        else:
            field_dict['field_name'] = x.name
            field_dict['field_type'] = type(x).__name__
            if x.verbose_name:
                field_dict['field_verbose_name'] = x.verbose_name
            else:
                field_dict['field_verbose_name'] = x.name
            if x.help_text:
                field_dict['field_helptext'] = x.help_text
            else:
                field_dict['field_helptext'] = x.name
            if field_dict['field_type'] in ['ForeignKey', 'ManyToManyField']:
                field_dict['related_class'] = f"{x.related_model.__name__}"
                field_dict['related_name'] = f"{x.related_query_name()}"
            model_fields.append(field_dict)
    return model_fields


def get_classdict_from_model(sample):
    """
    returns a dict describing a model and its fields
    :param sample: a model class
    """
    class_dict = {}
    class_dict['model_name'] = f"{sample.__name__}"
    class_dict['model_verbose_name'] = f"{sample._meta.verbose_name}"
    class_dict['model_helptext'] = f"{sample.__doc__.strip()}"
    class_dict['model_representation'] = False
    class_dict['model_order'] = False
    class_dict['model_fields'] = model_fields_to_dict(sample)
    return class_dict


def app_to_classdicts(app_name):
    class_dicts = []
    app_models = apps.get_app_config(app_name).get_models()
    for x in app_models:
        class_dicts.append(get_classdict_from_model(x))
    return class_dicts


def gsheet_to_df(sheet_id):
    url = f"{GDRIVE_BASE_URL}{sheet_id}&output=csv"
    r = requests.get(url)
    print(r.status_code)
    data = r.content
    df = pd.read_csv(BytesIO(data))
    return df


def df_to_classdicts(df):
    """
    parses an Excel sheet and yields dicts of model definitions
    :param df: a dataframe
    :return: yields dicts
    """
    classes = df.groupby('class name technical')
    for x in classes:
        local_df = x[1]
        class_dict = {}
        class_dict['model_name'] = x[0]
        class_dict['model_helptext'] = x[1]['class name helptext'].iloc[0].replace('\n', '')
        class_dict['model_verbose_name'] = x[1]['class name verbose_name'].iloc[0].replace('\n', '')
        try:
            source_table =  x[1]['source_table'].iloc[0]
        except KeyError:
            source_table = None
        if source_table is not None and isinstance(source_table, str):
            class_dict['source_table'] = source_table
        else:
            class_dict['source_table'] = None

        try:
            natural_primary_key =  x[1]['natural primary key'].iloc[0]
        except KeyError:
            natural_primary_key = 'legacy_id'
        if natural_primary_key is not None and isinstance(natural_primary_key, str):
            class_dict['natural_primary_key'] = natural_primary_key
        else:
            class_dict['natural_primary_key'] = "legacy_id"

        class_dict['model_representation'] = "{}".format(
            x[1]['class self representation'].iloc[0]
        ).lower()
        class_dict['model_order'] = "{}".format(
            x[1]['class object order by field'].iloc[0]
        ).lower()
        class_dict['model_fields'] = []
        for i, row in local_df.iterrows():
            org_field_name = row['field name technical'].lower().replace('/', '_').replace('|', '_')
            org_field_name = org_field_name.replace('__', '_')
            if org_field_name[0].isdigit():
                org_field_name = f"xx_{org_field_name}"
            field_name = org_field_name.replace('-', '_').replace('\n', '').replace(' ', '')
            if isinstance(field_name, str) and isinstance(row['field type'], str):
                field = {}
                field['field_name'] = field_name
                # public yes / no
                try:
                    field_public = row['public (yes|no)']
                except KeyError:
                    field_public = "yes"
                if field_public is not None and isinstance(field_public, str):
                    if 'yes' in field_public:
                        field['field_public'] = True
                    elif 'no' in field_public:
                        field['field_public'] = False
                    else:
                        field['field_public'] = True
                else:
                    field['field_public'] = True

                # value from lookup
                try:
                    value_from = row['value from']
                except KeyError:
                    value_from = None
                if value_from is not None and isinstance(value_from, str):
                    field['value_from'] = value_from.replace('\n', '').replace(' ', '').replace('\\', '/')
                else:
                    field['value_from'] = False

                # maps to arche
                try:
                    arche_prop = row['maps to ARCHE']
                except KeyError:
                    arche_prop = None
                if arche_prop is not None and isinstance(arche_prop, str):
                    field['arche_prop'] = arche_prop.replace('\n', '').replace(' ', '')
                else:
                    field['arche_prop'] = False
                try:
                    arche_prop_str_template = row['Mapping extra app work']
                except KeyError:
                    arche_prop_str_template = None
                if arche_prop_str_template is not None and isinstance(arche_prop_str_template, str):
                    field['arche_prop_str_template'] = arche_prop_str_template.replace('\n', '')
                else:
                    field['arche_prop_str_template'] = False

                # field type
                if ' ' in row['field type'].strip():
                    continue
                if row['field type'].startswith('Bool'):
                    field['field_type'] = 'BooleanField'
                elif '|' in row['field type']:
                    field_type = row['field type'].split('|')[0]
                    if field_type == 'FK':
                        field['field_type'] = 'ForeignKey'
                    else:
                        field['field_type'] = 'ManyToManyField'

                    # through param
                    if '#' in row['field type']:
                        rel_class = row['field type'].split('|')[1]
                        field['through'] = "".join(rel_class.split('#'))
                        field['related_class'] = rel_class.split('#')[0]
                    else:
                        field['related_class'] = row['field type'].split('|')[1].split(':')[0].strip()
                        temp_related_name = "rvn_{}_{}_{}".format(
                            x[0].lower(),
                            field_name,
                            field['related_class'].lower().strip()
                        ).replace('__', '_')
                    field['related_name'] = temp_related_name
                elif row['field type'] == "URI":
                    field['field_type'] = "CharField"
                elif row['field type'].startswith('Integ'):
                    field['field_type'] = "IntegerField"
                elif row['field type'].startswith('Float'):
                    field['field_type'] = "FloatField"
                elif row['field type'].startswith('Point'):
                    field['field_type'] = "PointField"
                elif row['field type'].startswith('TextF'):
                    field['field_type'] = "TextField"
                elif row['field type'].startswith('DateR'):
                    field['field_type'] = "DateRangeField"
                elif row['field type'].startswith('Date'):
                    field['field_type'] = "DateField"
                elif row['field type'] == "CharField":
                    field['field_type'] = "CharField"
                elif row['field type'] == "ChoiceField":
                    if isinstance(row['choices'], str):
                        field['choices'] = ast.literal_eval(row['choices'])
                    field['field_type'] = "CharField"
                else:
                    continue
                if isinstance(row['verbose field name'], str):
                    field['field_verbose_name'] = row['verbose field name'].replace('\n', '')
                else:
                    field['field_verbose_name'] = field_name
                if isinstance(row['helptext'], str):
                    field['field_helptext'] = row['helptext'].replace('\n', '')
                else:
                    field['field_helptext'] = f"helptext for {field_name}"

                class_dict['model_fields'].append(field)
        yield class_dict


def serialize_data_model(dicts, app_name="my_app", file_name='models.py'):
    t = Template(code_templates.MODELS_PY)
    output = t.render(
        data=dicts,
        app_name=app_name
    )
    with open(file_name, "w") as text_file:
        print(output, file=text_file)
    return file_name


def serialize_admin(dicts, app_name="my_app", file_name='admin.py'):
    t = Template(code_templates.ADMIN_PY)
    output = t.render(
        data=dicts,
        app_name=app_name
    )
    with open(file_name, "w") as text_file:
        print(output, file=text_file)
    return file_name


def serialize_tables(dicts, app_name="my_app", file_name='tables.py'):
    t = Template(code_templates.TABLES_PY)
    output = t.render(
        data=dicts,
        app_name=app_name
    )
    with open(file_name, "w") as text_file:
        print(output, file=text_file)
    return file_name


def serialize_views(dicts, app_name="my_app", file_name='views.py'):
    t = Template(code_templates.VIEWS_PY)
    output = t.render(
        data=dicts,
        app_name=app_name
    )
    with open(file_name, "w") as text_file:
        print(output, file=text_file)
    return file_name


def serialize_forms(dicts, app_name="my_app", file_name='forms.py'):
    t = Template(code_templates.FORMS_PY)
    output = t.render(
        data=dicts,
        app_name=app_name
    )
    with open(file_name, "w") as text_file:
        print(output, file=text_file)
    return file_name


def serialize_filters(dicts, app_name="my_app", file_name='filters.py'):
    t = Template(code_templates.FILTERS_PY)
    output = t.render(
        data=dicts,
        app_name=app_name
    )
    with open(file_name, "w") as text_file:
        print(output, file=text_file)
    return file_name


def serialize_urls(dicts, app_name="my_app", file_name='urls.py'):
    t = Template(code_templates.URLS_PY)
    output = t.render(
        data=dicts,
        app_name=app_name
    )
    with open(file_name, "w") as text_file:
        print(output, file=text_file)
    return file_name


def serialize_dal_views(dicts, app_name="my_app", file_name='urls.py'):
    t = Template(code_templates.DAL_VIEW_PY)
    output = t.render(
        data=dicts,
        app_name=app_name
    )
    with open(file_name, "w") as text_file:
        print(output, file=text_file)
    return file_name


def serialize_dal_urls(dicts, app_name="my_app", file_name='urls.py'):
    t = Template(code_templates.DAL_URLS_PY)
    output = t.render(
        data=dicts,
        app_name=app_name
    )
    with open(file_name, "w") as text_file:
        print(output, file=text_file)
    return file_name


# code example on how to use it:

# from appcreator import creator
# classdict = creator.app_to_classdicts("my_app")
# for x in dir(creator):
#     if x.startswith('seri'):
#         func = getattr(creator, x)
#         func(classdict, app_name="my_app")
