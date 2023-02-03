from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from random import randint
from .models import Card, UserProgress
from .forms import CardForm


class HomePageView(TemplateView):
    template_name = "home.html"


class CardListView(LoginRequiredMixin, ListView):
    model = Card


class CardDetailView(LoginRequiredMixin, DetailView):
    model = Card


@login_required
def practice(request):
    current_user = request.user
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            submitted_solved = form.cleaned_data["solved"]
            submitted_card_id = form.cleaned_data["card_id"]
            user_progress = UserProgress(
                user=current_user,
                card=Card.objects.get(id=submitted_card_id),
                is_understood=submitted_solved,
            )
            user_progress.save()

    # generate random card, we will need to exclude the cards that are stored in UserProgress
    cards_understood_ids = list(
        UserProgress.objects.filter(user=current_user).values_list("card_id", flat=True)
    )
    # get total number of cards
    total_cards = Card.objects.count()
    # get all cards ids
    all_cards_ids = Card.objects.all().values_list("id", flat=True)
    # random number from total number of cards
    random_index = randint(0, total_cards - 1)
    # check to see if the item at random_index in all_cards_ids is already understood
    while all_cards_ids[random_index] in cards_understood_ids:
        random_index = randint(0, total_cards - 1)

    # this ^ works, now we need an exit strategy when there are no more cards

    random_card = Card.objects.all()[random_index]

    context = {
        "user": current_user,
        "random_card": random_card,
    }
    return render(request, "cards/question.html", context)
