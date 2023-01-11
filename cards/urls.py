from django.contrib import admin
from django.urls import path, include

from .views import CardListView, random_card

urlpatterns = [
    path("", CardListView.as_view(), name="card-list"),
    path("random/", random_card, name="random-card"),
]
