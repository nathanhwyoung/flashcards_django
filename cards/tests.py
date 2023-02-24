from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from accounts.models import CustomUser
from .models import Card, UserProgress, Site
from datetime import datetime

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "HOME")
        
        
class SiteTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.site = Site.objects.create(url="https://www.google.com/")
        
    def test_model_content(self):
        self.assertEqual(self.site.url, "https://www.google.com/")
        
class CardTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        site = Site.objects.create(url="https://www.google.com/")
        cls.card = Card.objects.create(question="what is django?", answer="it's a web framework", url=site)

    def test_model_content(self):
        self.assertEqual(self.card.question, "what is django?")
        self.assertEqual(self.card.answer, "it's a web framework")
        
# these tests could use some work
class UserProgressTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        site = Site.objects.create(url="https://www.google.com/")
        card = Card.objects.create(question="what is django?", answer="it's a web framework", url=site)
        cls.user_progress = UserProgress.objects.create(
            user = CustomUser.objects.create(username="testuser"),
            card = card,
            is_understood = True,
            date_first_seen = datetime.now(),
            date_last_seen = datetime.now(),
            date_understood = datetime.now(),
            times_seen = 3,
        )
        
    def test_model_content(self):
        self.assertEqual(self.user_progress.user.username, "testuser")
        