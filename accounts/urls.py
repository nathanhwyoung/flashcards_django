from django.urls import path
from .views import SignupPageView, AccountView

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    path("account/", AccountView.as_view(), name="account"),
]
