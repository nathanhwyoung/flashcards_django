from django.urls import path, include
from .views import (
    CardListView,
    HomePageView,
    CardDetailView,
    leaderboard,
    practice,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("practice/", practice, name="practice"),
    path("detail/<int:pk>", CardDetailView.as_view(), name="card-detail"),
    path("all_cards/", CardListView.as_view(), name="card-list"),
    path("leaderboard/", leaderboard, name="leaderboard"),
]
