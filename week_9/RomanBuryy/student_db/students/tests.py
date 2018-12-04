from django.test import TestCase, Client
from django.urls import reverse

from .models import Student
# Create your tests here.

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            first_name = "test first_name",
            second_name = "test second_name",
            birthday = "1983-12-08",
            notes = "test notes"

        )

    def test_student_exist(self):
        student = Student.objects.get(first_name = "test first_name")
        self.assertEqual(student.second_name, "test second_name")



class StudentCreateViewTest(TestCase):
    def setUp(self):
        client = Client()



    def test_student_created(self):
        response = self.client.post(reverse('add_student'),
                                    {"fir4st_name":"test first_name", "second_name":"test second_name"})
        print(response)
        self.assertEqual(response.status_code, 200)
