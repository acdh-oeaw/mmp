from django.core.management.base import BaseCommand


from archiv.models import KeyWord


class Command(BaseCommand):
    help = "Create app files"

    def handle(self, *args, **kwargs):
        lookup_dict = {
            "Schlagwort": "Keyword",
            "Eigenname": "Name",
            "Unsicher": "unclear"
        }
        for key, value in lookup_dict.items():
            for x in KeyWord.objects.filter(art=key):
                x.art = value
                x.save()
                print(x.art)

        print("Done")
