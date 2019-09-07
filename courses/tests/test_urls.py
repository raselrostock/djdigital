from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from courses.views import (
    CourseListView
)
from django.test import Client


class TestUrls(TestCase):

    def test_courses_page_status_code(self):
        client = Client()
        response = self.client.get('courses/')
        self.assertEquals(response.status_code, 200)

    def test_courses_url_by_name(self):
        client = Client()
        response = self.client.get(reverse('courses:courselist'))
        self.assertEquals(response.status_code, 200)

    def test_courses_use_correct_template(self):
        client = Client()
        response = self.client.get(reverse('courses:courselist'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/course_list.html')
