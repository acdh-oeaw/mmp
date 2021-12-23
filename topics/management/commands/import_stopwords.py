import pandas as pd
from django.core.management.base import BaseCommand

from topics.models import StopWord


class Command(BaseCommand):
    help = "import stop words"

    def handle(self, *args, **kwargs):
        file = '~/Downloads/Acdh version Stoppwörter - lg vw Kopie 22122021.xlsx'

        df = pd.read_excel(file)
        for i, row in df.iterrows():
            try:
                word, value = row['token'].split(':')
            except ValueError:
                continue
            value = int(value)
            if value > 20:
                StopWord.objects.get_or_create(word=word)
