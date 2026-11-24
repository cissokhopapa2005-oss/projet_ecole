# School Manager

Application Django de consultation et de gestion des étudiants et des enseignants de l'école.

## Prérequis

- Python 3.10 ou supérieur
- pip

## Installation sous Windows (PowerShell)

Depuis le dossier `projet_ecole` :

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
```

## Créer un compte d'administration

```powershell
python manage.py createsuperuser
```

## Lancer le serveur

```powershell
python manage.py runserver
```

Ouvrir ensuite http://127.0.0.1:8000/.

## URLs disponibles

- `/` : accueil avec le nombre d'étudiants
- `/about/` : présentation
- `/students/` : liste et recherche par nom ou prénom
- `/students/<id>/` : fiche d'un étudiant
- `/students/classe/<classe>/` : étudiants d'une classe
- `/teachers/` : liste des enseignants
- `/admin/` : administration des étudiants et enseignants
