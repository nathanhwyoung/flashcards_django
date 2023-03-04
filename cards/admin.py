from django.contrib import admin
from .models import WebSite, Card, UserProgress

class WebSiteAdmin(admin.ModelAdmin):
    pass

class CardAdmin(admin.ModelAdmin):
    pass

class UserProgressAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(WebSite, WebSiteAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(UserProgress, UserProgressAdmin)
