from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import Stelle


class Command(BaseCommand):
    help = "Create app files"

    def handle(self, *args, **kwargs):
        to_process = Stelle.objects.filter(text__text_lang='lat')
        print(f"Stelle objects to process: {to_process.count()}")
        for x in tqdm(to_process, total=to_process.count()):
            x.save()
