from django.contrib import admin
from django.urls import path, include

from .views import CardListView, HomePageView, random_card

urlpatterns = [
    # path("", random_card, name="random-card"),
    path("", HomePageView.as_view(), name="home"),
    path("all_cards/", CardListView.as_view(), name="card-list"),
]
