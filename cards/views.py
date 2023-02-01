from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.shortcuts import render
from random import randint
from .models import Card


class HomePageView(TemplateView):
    template_name = "home.html"


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all()


def practice(request):
    # this view will need to exclude cards that have been marked as completed for the active user
    total_cards = Card.objects.count()
    random_index = randint(0, total_cards - 1)
    random_card = Card.objects.all()[random_index]
    context = {"random_card": random_card}
    return render(request, "cards/question.html", context)
