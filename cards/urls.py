from django.contrib import admin
from django.urls import path, include

from .views import CardListView, HomePageView, practice

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("practice/", practice, name="practice"),
    path("all_cards/", CardListView.as_view(), name="card-list"),
]
