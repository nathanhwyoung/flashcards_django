from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.shortcuts import render
from cards.views import Card


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "account/signup.html"


@login_required
def account(request):
    user = request.user
    context = {
        "user": user,
    }
    return render(request, "account/account.html", context)
