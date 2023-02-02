from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView

# from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from random import randint
from .models import Card

# User = get_user_model()


class HomePageView(TemplateView):
    template_name = "home.html"


class CardListView(LoginRequiredMixin, ListView):
    model = Card


class CardDetailView(LoginRequiredMixin, DetailView):
    model = Card


@login_required
def practice(request):
    # this view will need to exclude cards that have been marked as completed for the active user
    # total_cards = Card.objects.count()
    # random_index = randint(0, total_cards - 1)
    # random_card = Card.objects.all()[random_index]
    # context = {"random_card": random_card}
    user = request.user
    context = {"user": user}
    return render(request, "cards/question.html", context)
