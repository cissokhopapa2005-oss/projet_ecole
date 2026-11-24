from django.test import TestCase
from django.urls import reverse

from .models import Student


class StudentCrudTests(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="Awa",
            last_name="Diop",
            email="awa.diop@ecole.sn",
            phone="771234567",
            classe="L1",
        )

    def test_phone_validation_rejects_invalid_number(self):
        response = self.client.post(
            reverse("students:create"),
            {
                "first_name": "Moussa",
                "last_name": "Ndiaye",
                "email": "moussa.ndiaye@ecole.sn",
                "phone": "77-12",
                "classe": "L1",
                "active": "on",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Le numéro doit contenir 9 chiffres")
        self.assertFalse(Student.objects.filter(email="moussa.ndiaye@ecole.sn").exists())

    def test_update_keeps_same_student(self):
        response = self.client.post(
            reverse("students:update", args=[self.student.id]),
            {
                "first_name": "Awa",
                "last_name": "Diop",
                "email": "awa.diop@ecole.sn",
                "phone": "77 123 45 67",
                "classe": "L2",
                "active": "on",
            },
        )
        self.assertRedirects(response, reverse("students:detail", args=[self.student.id]))
        self.student.refresh_from_db()
        self.assertEqual(self.student.classe, "L2")
        self.assertEqual(self.student.phone, "771234567")
        self.assertEqual(Student.objects.count(), 1)

    def test_delete_requires_post(self):
        response = self.client.get(reverse("students:delete", args=[self.student.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Student.objects.filter(id=self.student.id).exists())

        response = self.client.post(reverse("students:delete", args=[self.student.id]))
        self.assertRedirects(response, reverse("students:list"))
        self.assertFalse(Student.objects.filter(id=self.student.id).exists())
