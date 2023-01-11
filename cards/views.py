from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Card, Site
from django.shortcuts import render

from random import randint


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all()


def random_card(request):
    total_cards = Card.objects.count()
    random_index = randint(0, total_cards - 1)
    random_card = Card.objects.all()[random_index]
    context = {"random_card": random_card}
    return render(request, "cards/random.html", context)
