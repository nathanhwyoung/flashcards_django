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

            if UserProgress.objects.filter(
                user=current_user, card=Card.objects.get(id=submitted_card_id)
            ).exists():
                UserProgress.objects.filter(
                    user=current_user, card=Card.objects.get(id=submitted_card_id)
                ).update(is_understood=submitted_solved)
            else:
                UserProgress.objects.create(
                    user=current_user,
                    card=Card.objects.get(id=submitted_card_id),
                    is_understood=submitted_solved,
                )

    # generate random card, exclude the cards that are stored in UserProgress
    cards_understood_ids = list(
        UserProgress.objects.filter(user=current_user, is_understood=True).values_list(
            "card_id", flat=True
        )
    )
    # get total number of cards
    total_cards = Card.objects.count()
    # get all cards ids
    all_cards_ids = Card.objects.all().values_list("id", flat=True)
    # random number from total number of cards
    random_index = randint(0, total_cards - 1)
    # get num of cards not understood
    cards_left = total_cards - len(cards_understood_ids)

    # check to see if the item at random_index in all_cards_ids is already understood
    if cards_left > 0:
        while all_cards_ids[random_index] in cards_understood_ids:
            random_index = randint(0, total_cards - 1)
        random_card = Card.objects.all()[random_index]
        context = {
            "user": current_user,
            "random_card": random_card,
        }
        return render(request, "cards/question.html", context)

    # implement success page to congratulate user
    return redirect("/")
