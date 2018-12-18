from django.test import TestCase
from .models import MineralModel, RockModel, Article
from django.contrib.auth.models import User

from django.urls import reverse


class MineralModelCreationTestCase(TestCase):

    def setUp(self):
        MineralModel.objects.create(
            name='Name',
            formula='formula',
            colour='colour',
            luster='luster',
            streak='streak',
            hardness=2,
            density=2,
            avatar='image',
            description='text'
        )

    def test_exist_mineral(self):

        """Checking the existence of a mineral in the database"""

        mineral = MineralModel.objects.get(name='Name')

        self.assertIsNotNone(mineral)
        self.assertIsInstance(mineral, MineralModel)

        self.assertEqual(mineral.avatar, 'image')


class RockModelCreationTest(TestCase):

    def setUp(self):
        RockModel.objects.create(
            name='name',
            min_composition='some composition',
            type='type',
            description='description',
            avatar='image'
        )

    def test_exist_rock(self):

        """Checking the existence of a rock in the database"""

        rock = RockModel.objects.get(name='name')

        self.assertIsNotNone(rock)
        self.assertIsInstance(rock, RockModel)

        self.assertEqual(rock.type, 'type')


class ArticleModelCreationTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('ROMA', 'mail@mail.com', 'password')

        Article.objects.create(
            title='title',
            body='description',
            author=self.user
        )

    def test_article_exist(self):

        """Checking the existence of a article in the database"""

        article = Article.objects.get(title='title')

        self.assertIsNotNone(article)
        self.assertIsInstance(article, Article)

        self.assertEqual(article.title, 'title')
        self.assertEqual(article.author.username, 'ROMA')


class HomePageViewTest(TestCase):

    def setUp(self):
        pass

    def test_homepage(self):

        """Checking that homepage return status code 200 and render correct template"""

        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_page.html')


class MineralListViewTest(TestCase):

    def setUp(self):
        pass

    def test_view_url_exist(self):

        """Checking that minerals database page return status code 200 and render correct template"""

        response = self.client.get(reverse('list_minerals'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'minerals.html')

    def test_show_entries(self):

        """Checking whether our database of minerals entries show up on the page"""

        MineralModel.objects.create(
            name='Name',
            formula='formula',
            colour='colour',
            luster='luster',
            streak='streak',
            hardness=2,
            density=2,
            avatar='image',
            description='text'
        )
        MineralModel.objects.create(
            name='Name2',
            formula='formula2',
            colour='colour2',
            luster='luster2',
            streak='streak2',
            hardness=2,
            density=2,
            avatar='image2',
            description='text2'
        )
        response = self.client.get(reverse('list_minerals'))

        self.assertContains(response, 'Name')
        self.assertContains(response, 'Name2')

    def test_show_entries_fail(self):

        """Test for empty database"""

        response = self.client.get(reverse('list_minerals'))
        self.assertContains(response, 'Sorry the database of minerals are empty.')


class MineralDetailViewTest(TestCase):

    def setUp(self):
        self.mineral = MineralModel.objects.create(
            name='Name',
            formula='formula',
            colour='colour',
            luster='luster',
            streak='streak',
            hardness=2,
            density=2,
            avatar='image',
            description='text'
        )

    def test_view_url_exist(self):
        """Checking that content page return status code 200 and render correct template"""

        response = self.client.get(self.mineral.get_absolute_url())

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mineral_data.html')

    def test_show_content(self):

        """Test whether out content show up on page"""

        response = self.client.get(self.mineral.get_absolute_url())

        self.assertContains(response, self.mineral.name)
        self.assertContains(response, self.mineral.description)


class RockListViewTest(TestCase):

    def setUp(self):
        pass

    def test_view_url_exist(self):

        """Checking that rocks database page return status code 200 and render correct template"""

        response = self.client.get(reverse('list_rocks', kwargs={'type': "type"}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rocks.html')

    def test_show_entries(self):

        """Checking whether our database rocks entries show up on the page"""
        self.rock = RockModel.objects.create(
            name='name',
            min_composition='composition',
            type='type',
            description='text',
            avatar='img'
        )
        response = self.client.get(reverse('list_rocks', kwargs={'type': "type"}))

        self.assertContains(response, 'name')

    def test_show_entries_fail(self):

        """Test for empty database"""

        response = self.client.get(reverse('list_rocks', kwargs={'type': "type"}))
        self.assertContains(response, 'Sorry the database are empty.')


class RockDetailViewTest(TestCase):

    def setUp(self):
        self.rock = RockModel.objects.create(
            name='name',
            min_composition='composition',
            type='type',
            description='text',
            avatar='img'
        )

    def test_view_url_exist(self):
        """Checking that content page return status code 200 and render correct template"""

        response = self.client.get(self.rock.get_absolute_url())

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rock_data.html')

    def test_show_content(self):

        """Test whether out content show up on page"""

        response = self.client.get(self.rock.get_absolute_url())

        self.assertContains(response, self.rock.description)


class CreateArticleViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('ROMA', 'mail@mail.com', 'password')
        if self.user.is_authenticated:
            Article.objects.create(
                title='title1',
                body='text1',
                author=self.user
            )
        self.client.login(username='ROMA', password='password')

    def test_view_url_exist(self):

        """Test whether our create article page return status code 200"""

        response = self.client.get(reverse('create_article'))

        self.assertEqual(response.status_code, 200)

    def test_create_article_if_user_is_authenticated(self):

        """Test creating new article if user is authenticated"""

        self.client.post(reverse('create_article'), {'title': "Title", 'body': "text", 'author': self.user})

        self.assertEqual(Article.objects.last().title, 'Title')
        self.assertEqual(Article.objects.last().author, self.user)

    def test_redirect(self):

        """ Test whether will happen redirect after creation article """

        response = self.client.post(reverse('create_article'), {'title': "Title", 'body': "text", 'author': self.user})
        self.assertEqual(response.status_code, 302)

    def test_create_article_if_user_is_not_authenticated(self):

        self.client.logout()
        response = self.client.get(reverse('create_article'))

        self.assertContains(response, 'Please log in if you wont post article')


class ArticleUpdateViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('ROMA', 'mail@mail.com', 'password')
        self.client.login(username='ROMA', password='password')
        self.article = Article.objects.create(
            title='title1',
            body='text1',
            author=self.user
        )
        self.article2 = Article.objects.create(
            title='title2',
            body='text2',
            author=self.user
        )

    def test_view_url_exist_if_user_is_authenticated(self):

        """Test whether our update article page return status code 200"""

        response = self.client.get(reverse('update', kwargs={'pk': self.article2.id}))

        self.assertEqual(response.status_code, 200)

    def test_update_article_if_user_is_authenticated(self):

        """Test update article if user is authenticated"""

        self.client.post(reverse('update', kwargs={'pk': self.article2.id}), {'title': "Title", 'body': "text", 'author': self.user})

        self.assertEqual(Article.objects.first().title, 'title1')
        self.assertEqual(Article.objects.last().title, 'Title')

    def test_view_url_exist_if_user_is_not_authenticated(self):

        """Test whether our update article page exist if user isn`t authenticated"""

        self.client.logout()
        with self.assertRaises(PermissionError):
            self.client.get(reverse('update', kwargs={'pk': self.article2.id}))


class ArticleDeleteViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('ROMA', 'mail@mail.com', 'password')
        self.client.login(username='ROMA', password='password')
        self.article = Article.objects.create(
            title='title1',
            body='text1',
            author=self.user
        )
        self.article2 = Article.objects.create(
            title='title2',
            body='text2',
            author=self.user
        )

    def test_view_url_exist_if_user_is_authenticated(self):

        """Test whether our delete article page exist"""

        response = self.client.get(reverse('delete', kwargs={'pk': self.article2.id}))

        self.assertEqual(response.status_code, 200)

    def test_delete_article_if_user_is_authenticated(self):

        """Test delete article if user is authenticated"""

        self.client.delete(reverse('delete', kwargs={'pk': self.article.id}))

        self.assertEqual(Article.objects.count(), 1)

    def test_view_url_exist_if_user_is_not_authenticated(self):

        """Test whether our delete article page exist if user isn`t authenticated"""

        self.client.logout()
        with self.assertRaises(PermissionError):
            self.client.get(reverse('delete', kwargs={'pk': self.article.id}))
