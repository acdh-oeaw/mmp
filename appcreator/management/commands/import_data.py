from sqlalchemy import create_engine
from django.core.management.base import BaseCommand
from django.conf import settings
from appcreator.import_utils import run_import

# imports for custom things
import json
from tqdm import tqdm
import pandas as pd
from django.core.serializers.json import DjangoJSONEncoder
from archiv.models import KeyWord, Stelle


dbc = settings.LEGACY_DB_CONNECTION
db_connection_str = f"mysql+pymysql://{dbc['USER']}:{dbc['PASSWORD']}@{dbc['HOST']}/{dbc['NAME']}"
db_connection = create_engine(db_connection_str)


class Command(BaseCommand):
    help = "Import Data"

    def handle(self, *args, **kwargs):
        run_import(
            'archiv',
            file_class_map_dict=None,
            limit=False
        )
        self.stdout.write(
            self.style.SUCCESS(
                'now start import custom things'
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                'KeyWords/Stichworte'
            )
        )

        query = "SELECT * FROM stichworte"
        df = pd.read_sql(query, con=db_connection)
        for i, row in tqdm(df.iterrows(), total=len(df)):
            item, _ = KeyWord.objects.get_or_create(legacy_pk=row['stid'])
            item.stichwort = row['stichwort']
            item.art = row['start']
            item.wurzel = row['wurzel']
            varianten = []
            for n in range(1,6):
                lookup = f"svar{n}"
                varianten.append(row[lookup].strip())
            item.varianten = ";".join(list(filter(None, varianten)))
            row_data = f"{json.dumps(row.to_dict(), cls=DjangoJSONEncoder)}"
            item.orig_data_csv = row_data
            item.save()

        self.stdout.write(
            self.style.SUCCESS(
                'link Stelle with KeyWords'
            )
        )
        query = "SELECT * FROM stelle"
        df = pd.read_sql(query, con=db_connection)
        stichwort_list = [x for x in list(df.keys()) if x.startswith('sstich')]
        ambique = []
        no_match = []
        for i, row in tqdm(df.iterrows(), total=len(df)):
            if row['sid']:
                try:
                    item = Stelle.objects.get(legacy_pk=row['sid'])
                except:
                    continue
                for st in stichwort_list:
                    if row[st] != "":
                        try:
                            lookup = row[st].strip()
                        except AttributeError:
                            continue
                        kws = KeyWord.objects.filter(stichwort=lookup)
                        if len(kws) == 1:
                            item.key_word.add(*kws)
                        else:
                            kws = KeyWord.objects.filter(
                                    varianten__contains=lookup
                                )
                            if len(kws) == 1:
                                item.key_word.add(*kws)
                            elif len(kws) > 1:
                                ambique.append(lookup)
                            else:
                                no_match.append(lookup)
                    else:
                        continue
        self.stdout.write(
            self.style.WARNING(
                f'ambigue:{set(ambique)}'
            )
        )
        self.stdout.write(
            self.style.WARNING(
                f'no matching KeyWord:{set(no_match)}'
            )
        )