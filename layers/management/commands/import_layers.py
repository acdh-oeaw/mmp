import glob
import json
import os
from django.core.management.base import BaseCommand

from layers.models import GeoJsonLayer


class Command(BaseCommand):
    help = "Import Layer Files"

    def handle(self, *args, **kwargs):

        files = glob.glob('./layers/geojson/*.json')
        for x in files:
            _, title = os.path.split(x)
            with open(x, 'r') as f:
                data = json.load(f)
            print(data.keys())
            _, item = GeoJsonLayer.objects.get_or_create(
                title=title, data=data
            )
            print(f"created Layer: {item}")

        print("Done")
