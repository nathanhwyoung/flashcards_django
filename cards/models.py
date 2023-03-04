from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class WebSite(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


class Card(models.Model):
    question = models.CharField(max_length=150)
    answer = models.TextField()
    url = models.ForeignKey(WebSite, on_delete=models.CASCADE)

    def __str__(self):
        return f"CARD ID: {self.id}, QUESTION: {self.question}"

    def get_absolute_url(self):
        return reverse("card-detail", args=[str(self.id)])


class UserProgress(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    is_understood = models.BooleanField(default=False)
    date_first_seen = models.DateTimeField(auto_now_add=True)
    date_last_seen = models.DateTimeField(auto_now=True)
    date_understood = models.DateTimeField(null=True)
    times_seen = models.IntegerField()

    def __str__(self):
        return f"CARD ID: {self.card.id}, USER: {self.user}, QUESTION: {self.card.question}, UNDERSTOOD: {self.is_understood}"

    class Meta:
        verbose_name_plural = 'User Progress'