from django.contrib import admin
from django.urls import path, include
from .views import CardListView, HomePageView, CardDetailView, practice

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("detail/<int:pk>", CardDetailView.as_view(), name="card-detail"),
    path("all_cards/", CardListView.as_view(), name="card-list"),
    path("practice/", practice, name="practice"),
]
