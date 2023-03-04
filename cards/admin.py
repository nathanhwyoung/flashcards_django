from django.contrib import admin
from .models import WebSite, Card, UserProgress


class WebSiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'url')

class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')

class UserProgressAdmin(admin.ModelAdmin):
    readonly_fields = ["date_first_seen", "date_last_seen", "date_understood", "times_seen"]
    list_display = ('id', 'user', 'card', 'is_understood')


# Register your models here.
admin.site.register(WebSite, WebSiteAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(UserProgress, UserProgressAdmin)
