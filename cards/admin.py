from django.contrib import admin
from .models import Site, Card, UserProgress

# Register your models here.
admin.site.register(Site)
admin.site.register(Card)
admin.site.register(UserProgress)
