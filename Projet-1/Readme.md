# Projet 1 – Analyse et Gestion des Coûts Médicaux

## Introduction

Ce projet consiste à développer une API RESTful pour la gestion et l'analyse des coûts médicaux à partir d'un jeu de données (*insurance.csv*). L'application repose sur :

- **SQLite** comme base de données,
- **SQLAlchemy** comme ORM,
- **FastAPI** pour l'exposition de l'API,
- **Faker** pour enrichir les données (noms, prénoms) de façon synthétique,
- **Pytest** pour les tests unitaires,
- **GitHub Actions** pour l'intégration continue (*linting* avec *flake8* et tests automatisés).

---

## Architecture du Projet

Le projet adopte une architecture modulaire avec plusieurs entités normalisées :

- **Sex** : Gère le sexe du patient (ex. "male", "female").
- **Region** : Gère la région d'appartenance du patient.
- **Smoker** : Gère le statut fumeur du patient (ex. "yes", "no").
- **AppUser** : Gère les comptes utilisateurs de l'application (nom d'utilisateur, mot de passe, e-mail).
- **Patient** : Contient les informations principales liées à la personne dont on analyse les coûts médicaux (nom, prénom, âge, BMI, charges, etc.).  
  - Référence (`sex_id`) vers l'entité **Sex**  
  - Référence (`region_id`) vers l'entité **Region**  
  - Référence (`smoker_id`) vers l'entité **Smoker**  
  - Optionnellement une référence (`user_id`) vers **AppUser** si le patient possède un compte

---

## Modèle de Données

### MCD, MLD, MPD

- **MCD (Modèle Conceptuel de Données)**
  - **Patient** : `id_patient`, `last_name`, `first_name`, `age`, `bmi`, `charges`, `children`, `sex_id`, `region_id`, `smoker_id`, `user_id`
  - **Sex** : `id_sex`, `sex_label`
  - **Region** : `id_region`, `region_name`
  - **Smoker** : `id_smoker`, `is_smoker`
  - **AppUser** : `id_user`, `username`, `password`, `user_email`

- **MLD (Modèle Logique de Données)**
  - Table **sex** : PK `id_sex`
  - Table **region** : PK `id_region`
  - Table **smoker** : PK `id_smoker`
  - Table **app_user** : PK `id_user`
  - Table **patient** : PK `id_patient`, FKs `sex_id` (vers `sex`), `region_id` (vers `region`), `smoker_id` (vers `smoker`), `user_id` (vers `app_user`)

- **MPD (Modèle Physique de Données)**
  - Implémenté via SQLAlchemy (*modules/database.py*), en SQLite.

---

## Arborescence du Projet

```
mini-projet-1/
├── main.py                # Point d'entrée de l'application FastAPI
├── models/
│   ├── base.py            # Configuration SQLAlchemy
│   ├── sex_model.py       # Modèle Sex
│   ├── region_model.py    # Modèle Region
│   ├── smoker_model.py    # Modèle Smoker
│   ├── app_user_model.py  # Modèle AppUser
│   ├── patient_model.py   # Modèle Patient
├── modules/
│   ├── database.py        # Gestion de la base SQLite
│   ├── crud.py            # Opérations CRUD
├── routes/
│   ├── sex_routes.py      # Endpoints Sex
│   ├── region_routes.py   # Endpoints Region
│   ├── smoker_routes.py   # Endpoints Smoker
│   ├── app_user_routes.py # Endpoints AppUser
│   ├── patient_routes.py  # Endpoints Patient
├── scripts/
│   ├── import_data.py     # Script d'importation des données CSV + Faker
├── tests/
│   ├── test_sex.py        # Tests unitaires Sex
│   ├── test_region.py     # Tests unitaires Region
│   ├── test_smoker.py     # Tests unitaires Smoker
│   ├── test_app_user.py   # Tests unitaires AppUser
│   ├── test_patient.py    # Tests unitaires Patient
├── .github/
│   ├── workflows/
│   │   ├── main.yml       # Workflow GitHub Actions
├── .flake8                # Configuration du linting
├── requirements.txt       # Liste des dépendances
├── Dockerfile             # Dockerisation du projet
└── README.md              # Documentation du projet
```

---

## Installation et Configuration

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/mini-projet-1.git
cd mini-projet-1
```

### 2. Créer et activer un environnement virtuel

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
.\.venv\Scripts\activate  # Windows
```

### 3. Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. (Optionnel) Configurer *flake8*

Vous pouvez personnaliser les règles dans `.flake8`.

---

## Exécution de l'Application

```bash
uvicorn main:app --reload
```

---

## Importation des Données

```bash
python scripts/import_data.py
```

---

## Tests Unitaires

```bash
pytest
```

---

## Intégration Continue (GitHub Actions)

Le workflow `.github/workflows/main.yml` s'exécute à chaque *push* et *pull request* sur `main`.

---

## Contributions

Les contributions sont les bienvenues ! Pour contribuer, créez une *pull request*.

---

## Contributeur

- **Mathieu Soussignan**

---

## Licence

Ce projet est sous licence **MIT**.