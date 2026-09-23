from appcreator import creator
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Saves data model of passed in app as csv"

    def handle(self, *args, **kwargs):
        app_name = "archiv"
        df = creator.class_dicst_to_df(app_name)
        df.to_csv(f"{app_name}.csv", index=False)
