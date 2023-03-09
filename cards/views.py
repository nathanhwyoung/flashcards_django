from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from random import randint
from datetime import datetime
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
            submitted_understood = form.cleaned_data["understood"]
            submitted_card_id = form.cleaned_data["card_id"]

            up = UserProgress.objects.filter(
                user=current_user, card=Card.objects.get(id=submitted_card_id)
            )
            # if UP object exists, update it
            if up.exists():
                # if card is understood, update the date_understood datetime field
                if submitted_understood == True:
                    up.update(
                        is_understood=submitted_understood,
                        date_understood=datetime.now(),
                        times_seen=F("times_seen") + 1,
                    )
                # if not, simply update the object
                else:
                    up.update(
                        is_understood=submitted_understood,
                        times_seen=F("times_seen") + 1,
                    )
            # if UP object does NOT exist, create it
            else:
                if submitted_understood == True:
                    UserProgress.objects.create(
                        user=current_user,
                        card=Card.objects.get(id=submitted_card_id),
                        is_understood=submitted_understood,
                        date_understood=datetime.now(),
                        times_seen=1,
                    )
                else:
                    UserProgress.objects.create(
                        user=current_user,
                        card=Card.objects.get(id=submitted_card_id),
                        is_understood=submitted_understood,
                        times_seen=1,
                    )

    # generate random card, exclude the cards that are stored in UserProgress
    cards_understood_ids = list(
        UserProgress.objects.filter(user=current_user, is_understood=True).values_list(
            "card_id", flat=True
        )
    )
    
    # get total number of cards
    total_cards = Card.objects.count()
    
    if total_cards > 0:
    
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

        # add message to congratulate user if no cards are left
        messages.success(request, 'congratulations! you have mastered all of the cards.')
        return redirect("leaderboard")
    
    # add message and redirect
    messages.info(request, 'there are no cards in the stack right now.')
    return redirect("home")
    
    


@login_required
def leaderboard(request):
    users = get_user_model().objects.all()
    total_cards = Card.objects.all().count()
    leaderboard_data = []
    # for each user, query the db and append an object to the list
    for user in users:
        individual_query = UserProgress.objects.filter(user__username=user)
        if individual_query:
            # # of items completed
            cards_understood = 0
            for user_progress in individual_query:
                if user_progress.is_understood == True:
                    cards_understood += 1
            # % of items completed
            percentage_completed = cards_understood/total_cards
            percentage_completed_formatted = "{:.0%}".format(percentage_completed)
            leaderboard_data.append(
                {
                    "user": user.username,
                    "cards_understood": cards_understood,
                    "percentage_completed": percentage_completed_formatted,
                }
            )
    context = {
        "data": leaderboard_data
    }
    return render(request, "leaderboard.html", context)
    
