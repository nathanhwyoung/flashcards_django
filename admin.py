from django.contrib import admin

class FlashCardsAdminSite(admin.AdminSite):
    title_header = 'FlashCards Admin'
    site_header = 'FlashCards Administration'
    index_title = 'FlashCards Site Admin'