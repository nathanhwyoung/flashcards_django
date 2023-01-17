from django.contrib import admin
from django.urls import path, include

from .views import CardListView, random_card

urlpatterns = [
    path("", random_card, name="random-card"),
    path("all_cards/", CardListView.as_view(), name="card-list"),
]
