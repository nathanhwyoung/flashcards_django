from django.db import models
from django.contrib.auth import get_user_model


class Site(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


class Card(models.Model):
    question = models.CharField(max_length=150)
    answer = models.TextField()
    url = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class UserProgress(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    is_understood = models.BooleanField(default=False)

    def __str__(self):
        return f"USER: {self.user}, CARD: {self.card}, UNDERSTOOD: {self.is_understood}"
