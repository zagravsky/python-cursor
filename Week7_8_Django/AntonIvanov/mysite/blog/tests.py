from django.test import TestCase, Client
from .models import Article
from django.urls import reverse


class ArticleTestCase(TestCase):

    def setUp(self):
        Article.objects.create(
            title='Some Title',
            description='Some Description',
            author='Anton'
        )

    def test_article_exist(self):
        """
        Created article Exists jn  the database
        """
        article = Article.objects.get(title='Some Title')
        self.assertEqual(article.author, 'Anton')

class ArticleCreateViewTest(TestCase):

    # def setUp(self):
        # client = Client()

    def test_art_create(self):
        """
        Created article saved in database
        """
        response = self.client.post(reverse('add_article'),
            {'title': 'Test Title', 'description': 'Test Description', 'author': 'Test Author'}
        )
        self.assertEqual(response.status_code, 302)
