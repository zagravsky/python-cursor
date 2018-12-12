from django.test import TestCase, Client
from django.urls import reverse

from todolist.models import Todo, Profile
from datetime import datetime
from django.contrib.auth.models import User
import pytz


class TodoTestCase(TestCase):

    def setUp(self):
        self.username = 'john'
        self.password = '123'
        self.create_at = datetime.now(tz=pytz.utc)
        self.user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        Todo.objects.create(
            title='Test title',
            text='Test text',
            create_at=self.create_at,
            created_by=self.user
        )

    def test_todo_exist(self):
        """Created todo exists in DB"""
        todo = Todo.objects.get(title="Test title")
        self.assertEqual(todo.created_by, self.user)
        self.assertEqual(todo.create_at, self.create_at)
        self.assertEqual(todo.text, 'Test text')

    def test_todo_exist_fail(self):
        """Created todo did not exists in DB"""
        todo = Todo.objects.get(title="Test title")
        self.assertEqual(todo.created_by, self.user)
        self.assertEqual(todo.create_at, self.create_at)
        self.assertEqual(todo.text, 'Test texts')


class TodoAddViewTest(TestCase):

    def setUp(self):
        client = Client()
        self.username = 'john'
        self.password = '123'
        self.create_at = datetime.now(tz=pytz.utc)
        self.user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)

    def test_todo_created(self):
        """Created article saved in DB"""
        response = self.client.post(reverse('add'),
                                    {'title': 'Test title', 'text': 'Test text', 'create_at': self.create_at,
                                     'created_by': self.user})
        print(response)
        self.assertEqual(response.status_code, 200)

