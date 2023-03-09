from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.shortcuts import render
from cards.views import Card


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "account/signup.html"


# use UpdateView here at some point
# class AccountView(generic.ListView):
#     # form_class = CustomUserChangeForm
#     # model = CustomUser
#     # queryset = CustomUser.objects.all()
#     # success_url = reverse_lazy("profile")
#     template_name = "account/account.html"
#     model = CustomUser


@login_required
def account(request):
    user = request.user
    context = {
        "user": user,
    }
    return render(request, "account/account.html", context)
