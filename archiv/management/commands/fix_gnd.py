from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import Autor


class Command(BaseCommand):
    help = "Fixing GND-IDS"

    def handle(self, *args, **kwargs):
        items = Autor.objects.all()
        for x in tqdm(items, total=items.count()):
            x.save()
        print("Done")
