from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class CardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cards'
    
class CardsAdminConfig(AdminConfig):
    # this is the project level flashcards_django/admin.py file
    default_site = 'admin.FlashCardsAdminSite'
