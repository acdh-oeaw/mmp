from django.core.management.base import BaseCommand
from archiv.models import UseCase


class Command(BaseCommand):
    help = "sets show labels field"

    def handle(self, *args, **kwargs):
        use_case_ids = [3, 8, 9, 11, 12]
        for x in use_case_ids:
            item = UseCase.objects.get(id=x)
            print(item)
            item.show_labels = True
            item.save()
