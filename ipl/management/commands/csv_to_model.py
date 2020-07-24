from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from ipl.csv import csv_to_model1
        from ipl.csv import csv_to_model2
        csv_to_model1()
        csv_to_model2()
