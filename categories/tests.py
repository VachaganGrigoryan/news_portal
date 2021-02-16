from django.test import TestCase
from categories.models import Category


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="News", slug="news", parent=None)
        news = Category.objects.get(name="News")
        Category.objects.create(name="Politics", slug="politics", parent=news)
        Category.objects.create(name="Tech", slug="tech", parent=news)

    def test_data_output(self):
        news = Category.objects.get(name="News")
        politics = Category.objects.get(name="Politics")
        tech = Category.objects.get(name="Tech")

        self.assertEqual(str(news), '<Category: News>')
        self.assertEqual(str(politics), '<Category: News -> Politics>')
        self.assertEqual(str(tech), '<Category: News -> Tech>')
