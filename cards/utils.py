import csv

from cards.models import WebSite, Card


def import_cards():
    with open("props_django.csv", newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            if row[0]:
                new_site = WebSite.objects.create(url=row[0])
            else:
                new_card = Card.objects.create(
                    question=row[1], answer=row[2], url=new_site
                )
