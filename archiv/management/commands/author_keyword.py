import pandas as pd
from django.core.management.base import BaseCommand
from tqdm import tqdm


from archiv.models import Autor, KeyWord


class Command(BaseCommand):
    help = "Create app files"

    def handle(self, *args, **kwargs):
        items = Autor.objects.all()
        print("Saving each Autor Object to update start/end date year")
        for x in tqdm(items, total=items.count()):
            x.save()

        print("Update KeyWord Types")
        df = pd.read_csv('./keywords.csv')
        for i, row in tqdm(df.iterrows(), total=len(df)):
            item = KeyWord.objects.get(stichwort=row['Keyword'])
            item.art = row['type']
            item.save()

        print("Done")
