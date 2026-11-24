from django.test import TestCase
from django.urls import reverse

from .models import Teacher


class TeacherCrudTests(TestCase):
    def test_teacher_create(self):
        response = self.client.post(
            reverse("teachers:create"),
            {
                "first_name": "Fatou",
                "last_name": "Sow",
                "email": "fatou.sow@ecole.sn",
                "subject": "Mathématiques",
            },
        )
        self.assertRedirects(response, reverse("teachers:list"))
        self.assertTrue(Teacher.objects.filter(email="fatou.sow@ecole.sn").exists())
