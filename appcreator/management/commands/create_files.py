from django.core.management.base import BaseCommand
from django.conf import settings
from appcreator import creator


class Command(BaseCommand):
    help = "Create app files"

    def handle(self, *args, **kwargs):
        sheet_id = settings.SHEET_ID
        df = creator.gsheet_to_df(sheet_id)
        dicts = [x for x in creator.df_to_classdicts(df)]
        app_name = 'archiv'
        creator.serialize_dal_views(
            dicts, app_name=app_name, file_name=f"{app_name}/dal_views.py"
        )
        self.stdout.write(
            self.style.SUCCESS(
                'created dal_views'
            )
        )
        creator.serialize_dal_urls(
            dicts, app_name=app_name, file_name=f"{app_name}/dal_urls.py"
        )
        self.stdout.write(
            self.style.SUCCESS(
                'created dal_urls'
            )
        )
        creator.serialize_filters(
            dicts, app_name=app_name, file_name=f"{app_name}/filters.py"
        )
        self.stdout.write(
            self.style.SUCCESS(
                'created filters'
            )
        )
        creator.serialize_data_model(
            dicts, app_name=app_name, file_name=f"{app_name}/models.py"
        )
        self.stdout.write(
            self.style.SUCCESS(
                'created models'
            )
        )
        creator.serialize_admin(
            dicts, app_name=app_name, file_name=f"{app_name}/admin.py"
        )
        self.stdout.write(
            self.style.SUCCESS(
                'created admin'
            )
        )
        creator.serialize_tables(
            dicts, app_name=app_name, file_name=f"{app_name}/tables.py"
        )
        self.stdout.write(
            self.style.SUCCESS(
                'created tables'
            )
        )
        creator.serialize_views(
            dicts, app_name=app_name, file_name=f"{app_name}/views.py"
        )
        self.stdout.write(
            self.style.SUCCESS(
                'created views'
            )
        )
        creator.serialize_forms(
            dicts, app_name=app_name, file_name=f"{app_name}/forms.py"
        )
        self.stdout.write(
            self.style.SUCCESS(
                'created forms'
            )
        )
        creator.serialize_urls(
            dicts, app_name=app_name, file_name=f"{app_name}/urls.py"
        )
        self.stdout.write(
            self.style.SUCCESS(
                'created urls'
            )
        )
