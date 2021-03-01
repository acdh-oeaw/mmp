from sqlalchemy import create_engine
from django.core.management.base import BaseCommand
from django.conf import settings
from tqdm import tqdm
import pandas as pd
import math
import archiv

dbc = settings.LEGACY_DB_CONNECTION
db_connection_str = f"mysql+pymysql://{dbc['USER']}:{dbc['PASSWORD']}@{dbc['HOST']}/{dbc['NAME']}"
db_connection = create_engine(db_connection_str)


class Command(BaseCommand):
    help = "Import Data Plus"

    def handle(self, *args, **kwargs):
        query = "SELECT * FROM text"
        text_class = getattr(archiv.models, 'Text')
        df = pd.read_sql(query, con=db_connection)
        self.stdout.write(
            self.style.NOTICE(
                "Import additional Authors"
            )
        )
        rel_item_class = getattr(archiv.models, 'Autor')
        for i, row in df.query('tautor2 != ""').iterrows():
            cur_item = text_class.objects.get(legacy_pk=row['tID'])
            for x in ['tautor2', 'tautor3']:
                value = row[x]
                if value:
                    rel_item = rel_item_class.objects.get(legacy_pk=value)
                    rel_attr = getattr(cur_item, 'autor')
                    rel_attr.add(rel_item)

        self.stdout.write(
            self.style.NOTICE(
                "Import additional Orte"
            )
        )
        torte = [f"tort{i}" for i in range(2, 7)]
        rel_item_class = getattr(archiv.models, 'Ort')
        for i, row in df.query('tort2 != ""').iterrows():
            cur_item = text_class.objects.get(legacy_pk=row['tID'])
            for x in torte:
                value = row[x]
                if value:
                    rel_item = rel_item_class.objects.get(legacy_pk=value)
                    rel_attr = getattr(cur_item, 'ort')
                    rel_attr.add(rel_item)

        self.stdout.write(
            self.style.NOTICE(
                "remove nan from places"
            )
        )
        for x in archiv.models.Ort.objects.all():
            try:
                if math.isnan(x.long):
                    x.long = None
                    x.lat = None
                    x.save()
            except TypeError:
                pass

        self.stdout.write(
            self.style.NOTICE(
                "create display_label for Stelle"
            )
        )
        for x in tqdm(
            archiv.models.Stelle.objects.all(),
            total=archiv.models.Stelle.objects.all().count()
        ):
            x.save()
