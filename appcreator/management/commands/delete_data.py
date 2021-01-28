from django.core.management.base import BaseCommand

from appcreator.import_utils import delete_all


class Command(BaseCommand):
    help = "Import Data"

    def handle(self, *args, **kwargs):
        delete_all('archiv')
