from django.db import models


class Teacher(models.Model):
    first_name = models.CharField("prénom", max_length=100)
    last_name = models.CharField("nom", max_length=100)
    email = models.EmailField("email", unique=True)
    subject = models.CharField("matière", max_length=100)

    class Meta:
        ordering = ["last_name"]
        verbose_name = "enseignant"
        verbose_name_plural = "enseignants"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
