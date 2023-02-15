from django.contrib import admin
from django.urls import path, include
from .views import (
    CardListView,
    HomePageView,
    CardDetailView,
    UserProgressListView,
    practice,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("practice/", practice, name="practice"),
    path("detail/<int:pk>", CardDetailView.as_view(), name="card-detail"),
    path("all_cards/", CardListView.as_view(), name="card-list"),
    path("leaderboard/", UserProgressListView.as_view(), name="leaderboard"),
]
