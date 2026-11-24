from django.shortcuts import render
from students.models import Student


def home(request):
    return render(request, "pages/home.html", {
        "school_name": "ISEP Amadou Trawaré de Diamniadio",
        "nb_students": Student.objects.count(),
        "nb_active": Student.objects.filter(active=True).count(),
    })


def about(request):
    return render(request, "pages/about.html")
