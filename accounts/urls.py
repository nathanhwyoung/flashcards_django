from django.urls import path
from .views import SignupPageView, account

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    path("account/", account, name="account"),
    # path("account/", AccountView.as_view(), name="account"),
]
