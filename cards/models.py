from django.db import models


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
