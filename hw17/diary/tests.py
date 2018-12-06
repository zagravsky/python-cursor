from django.test import TestCase, Client
from django.urls import reverse
from .models import Post

# To run these tests execute in terminal (while in project directory): python manage.py test
# if you want more info - use "verbosity", e.g. : python manage.py test --verbosity=2


class IndexViewTest(TestCase):
    """ Tests for IndexView """

    def setUp(self):
        client = Client()

        for i in range(0, 3):
            post = Post.objects.create(
                title=f'Test title {i}',
                content=f'Test content {i}',
                author=f'Test author {i}',
            )
            post.save()

    def test_created_posts_shown(self):
        """ Check that all posts with all info are shown """
        for i in range(0, 3):
            response = self.client.get(reverse('index'))
            self.assertContains(response, f'Test title {i}')
            self.assertContains(response, f'Test content {i}')
            self.assertContains(response, f'Test author {i}')

    def test_incorrect_posts_not_shown(self):
        """ Check that posts with incorrect info are not shown"""
        response = self.client.get(reverse('index'))
        self.assertNotRegex(response.content.decode('utf-8'), 'Test title [^012]')


class PostContentViewTest(TestCase):
    """ Tests for PostContentView """

    def setUp(self):
        client = Client()

        for i in range(1, 3):
            post = Post.objects.create(
                title=f'Test title {i}',
                content=f'Test content {i}',
                author=f'Test author {i}',
            )
            post.save()

    def test_correct_content_shown(self):
        """ Check that specific post page shows correct info """
        response = self.client.get('/posts/1')  # 1 is an id of first post
        expected_response_content = b'\n<body background="/static/background2.jpg" style="padding-right:150; padding-left:150">\n<center><a href="/"><img src="/static/journal-logo.png" height="73" width="400"></a></center>\n<a href="/"><i>Back to Journal</i></a>\n<h2>Test title 1</h2>\n<h4><i>by: Test author 1</i></h4>\n<p>Test content 1</p>\n<br>\n<br>\n<br>\n<a href="/posts/update/1"><i>Edit</i></a>\n<br>\n<br>\n<a href="/posts/delete/1"><i>Delete</i></a>\n<br>\n<br>\n<a href="/posts/compose"><i>New post</i></a>\n\n'
        self.assertEqual(response.content, expected_response_content)

    def test_incorrect_content_shown(self):
        """ Check that specific post page does not show info of other post """
        response = self.client.get('/posts/2')  # 2 is an id of second post
        print('RESPONSE: ', response)
        self.assertNotContains(response, f'Test author 1')


class ComposePostViewTest(TestCase):
    """ Tests for ComposePostView """

    def setUp(self):
        client = Client()

        response = self.client.post(
            reverse('compose'),
            {'title': 'Test title', 'content': 'Test content', 'author': 'Test author'}
        )

    def test_post_created(self):
        """ Check that created post is saved in the database """
        try:  # try-except is used so that if test fails it is shown as FAIL not ERROR
            post = Post.objects.get(title='Test title')
            self.assertEqual(str(post), 'Test title by Test author')
        except Exception as e:
            self.fail('test has failed!')

    def test_only_one_post_created(self):
        """ Check that only one post is saved in the database """
        try:  # try-except is used so that if test fails it is shown as FAIL not ERROR
            post = Post.objects.get()
        except Exception as e:
            self.fail('test has failed!')


class UpdatePostViewTest(TestCase):
    """ Tests for UpdatePostView """

    def setUp(self):
        client = Client()

        for i in range(1, 3):
            post = Post.objects.create(
                title=f'Test title {i}',
                content=f'Test content {i}',
                author=f'Test author {i}',
            )
            post.save()

        response = self.client.post(
            reverse('update', kwargs={'pk': 1}),  # 1 is a post.id of first post
            {'title': 'Test title 1 updated', 'content': 'Test content 1 updated', 'author': 'Test author 1 updated'}
        )

    def test_post_updated(self):
        """ Check that updated post is saved in the database """
        try:  # try-except is used so that if test fails it is shown as FAIL not ERROR
            updated_post = Post.objects.get(title='Test title 1 updated')
            self.assertEqual(str(updated_post), 'Test title 1 updated by Test author 1 updated')
        except Exception as e:
            self.fail('test has failed!')

    def test_only_correct_post_updated(self):
        """ Check that other posts are not affected by update in the database """
        try:  # try-except is used so that if test fails it is shown as FAIL not ERROR
            updated_post = Post.objects.get(title='Test title 2')
            self.assertEqual(str(updated_post), 'Test title 2 by Test author 2')
        except Exception as e:
            self.fail('test has failed!')


class DeletePostViewTest(TestCase):
    """ Tests for DeletePostView """

    def setUp(self):
        client = Client()

        for i in range(1, 3):
            post = Post.objects.create(
                title=f'Test title {i}',
                content=f'Test content {i}',
                author=f'Test author {i}',
            )
            post.save()

        response = self.client.post(
            reverse('delete', kwargs={'pk': 1}),  # 1 is a post.id of first post
        )

    def test_post_deleted(self):
        """ Check that deleted post is not present in the database """
        try:  # try-except is used so that if test fails it is shown as FAIL not ERROR
            Post.objects.get(title='Test title 1')  # trying to get the deleted post from the database
        except Exception as e:
            self.assertEqual(str(e), 'Post matching query does not exist.')  # comparing with expected exception

    def test_only_correct_post_deleted(self):
        """ Check that other posts are not affected by delete """
        try:  # try-except is used so that if test fails it is shown as FAIL not ERROR
            Post.objects.get(title='Test title 2')  # trying to get the NOT deleted post from the database
        except Exception as e:
            self.fail('test has failed!')
