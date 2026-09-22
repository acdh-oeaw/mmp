from django.core.management.base import BaseCommand
from story_map.import_utils import import_from_knlab


class Command(BaseCommand):
    help = 'Imports Story Map data from knightlab URL'

    def add_arguments(self, parser):

        parser.add_argument(
            '--url',
            default="https://uploads.knightlab.com/storymapjs/ee3762a02e5862af8f02906ab1d35ec6/mapping-medieval-people-alternative-map/draft.json",  # noqa: E501
            help='URL to fetch data',
        )
        parser.add_argument(
            '--story',
            default="Default Story Map",
            help='Title of the Story Map',
        )

    def handle(self, *args, **kwargs):
        url = kwargs['url']
        story_title = kwargs['story']
        msg = f"Downloading data from URL: {url} for story map {story_title}"
        self.stdout.write(self.style.NOTICE(f"{msg}"))
        slides = import_from_knlab(url, story_title)
        self.stdout.write(self.style.SUCCESS(f"created {len(slides)} slides"))
