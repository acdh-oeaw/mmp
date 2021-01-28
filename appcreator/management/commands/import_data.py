from sqlalchemy import create_engine
from django.core.management.base import BaseCommand
from django.conf import settings

from appcreator.import_utils import run_import

dbc = settings.LEGACY_DB_CONNECTION 
db_connection_str = f"mysql+pymysql://{dbc['USER']}:{dbc['PASSWORD']}@{dbc['HOST']}/{dbc['NAME']}"
db_connection = create_engine(db_connection_str)


class Command(BaseCommand):
    help = "Import Data"

    def handle(self, *args, **kwargs):
        run_import('archiv', file_class_map_dict=None)
