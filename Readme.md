## Application Globale – Gestion, Prédiction et Orchestration des Coûts Médicaux

## Table des Matières
1. [Introduction](#introduction)
2. [Projet 1 – Analyse et Gestion des Coûts Médicaux](#projet-1--analyse-et-gestion-des-couts-medicaux)
3. [Projet 2 – Benchmarking et Déploiement de Modèles d’IA](#projet-2--benchmarking-et-deploiement-de-modeles-dia)
4. [Projet 3 – Orchestration et Journalisation](#projet-3--orchestration-et-journalisation)
5. [Architecture Globale](#architecture-globale)
6. [Installation et Lancement](#installation-et-lancement)
7. [Utilisation](#utilisation)
8. [Auteur](#auteur)
9. [Contributions](#contributions)
10. [Licence](#licence)

### Introduction
Cette application globale se compose de trois projets complémentaires :

### Projet 1 – Analyse et Gestion des Coûts Médicaux
Une API RESTful développée avec FastAPI, qui permet de gérer et d’analyser les données médicales à partir du dataset `insurance.csv`. Le projet utilise SQLite, SQLAlchemy, Faker (pour générer des données synthétiques), Pytest et GitHub Actions pour l’intégration continue.

### Projet 2 – Benchmarking et Déploiement de Modèles d’IA
Ce projet vise à prédire les charges médicales (la target) en entraînant plusieurs modèles de machine learning (par exemple, régression linéaire et Random Forest). Il intègre le prétraitement des données, l’évaluation avec des métriques (RMSE, MAE, R²), le suivi des expérimentations via MLflow, et la sauvegarde du modèle le plus performant pour le déploiement.

### Projet 3 – Orchestration et Journalisation
Une application Streamlit qui sert d’interface utilisateur pour orchestrer les appels aux API des Projets 1 et 2. Elle permet de récupérer les données patients, de lancer des prédictions en temps réel et de visualiser les résultats, tout en journalisant les actions via loguru. Un fichier `docker-compose.yml` permet de déployer les trois services ensemble dans un réseau commun.

## Architecture Globale
L’architecture se présente ainsi :

### API Projet 1 (Gestion des données)
- **Technologies** : FastAPI, SQLite, SQLAlchemy
- **Rôle** : Gestion des entités (`Sex`, `Region`, `Smoker`, `AppUser`, `Patient`) et exposition d’un ensemble d’endpoints pour la création, la lecture, la mise à jour et la suppression.

### API Projet 2 (Prédiction des charges)
- **Technologies** : FastAPI, Scikit-Learn (ou Keras), MLflow
- **Rôle** : Entraînement, évaluation et déploiement d’un modèle de machine learning pour prédire les charges médicales. Un pipeline complet (préprocesseur + modèle) est sauvegardé pour être utilisé en production.

### Application Projet 3 (Orchestration et Interface Utilisateur)
- **Technologies** : Streamlit, Requests, Loguru
- **Rôle** : Orchestration des appels vers les API des Projets 1 et 2, gestion interactive des prédictions (formulaires avancés, visualisations interactives avec Altair) et export/import de résultats.
- **Déploiement multi-container** : Grâce à Docker Compose, les trois projets sont déployés sur un réseau commun, facilitant ainsi la communication entre eux.

## Installation et Lancement

### En local (hors Docker)
Cloner le dépôt global :
```bash
git clone https://github.com/votre-utilisateur/mini-projet-application.git
cd mini-projet-application
```

Configurer et lancer chaque projet individuellement :

#### Projet 1 (API de gestion) :
```bash
cd Projet-1
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```
Accessible sur [http://localhost:8001](http://localhost:8001).

#### Projet 2 (API de prédiction) :
```bash
cd ../Projet-2
uvicorn main:app --host 0.0.0.0 --port 8002 --reload
```
Accessible sur [http://localhost:8002](http://localhost:8002).

#### Projet 3 (Interface Streamlit) :
```bash
cd ../Projet-3
streamlit run app.py --server.port=8501
```
Accessible sur [http://localhost:8501](http://localhost:8501).

### Via Docker Compose
Un fichier `docker-compose.yml` est fourni à la racine du dépôt global pour lancer les trois services simultanément.

Construire et lancer les services :
```bash
docker-compose up --build
```

Accéder aux services :
- **API Projet 1** : [http://localhost:8001](http://localhost:8001)
- **API Projet 2** : [http://localhost:8002](http://localhost:8002)
- **Interface Projet 3** : [http://localhost:8501](http://localhost:8501)

## Utilisation

### API Projet 1 :
Permet la gestion des données médicales via des endpoints REST (ex. `/utilisateurs/`, `/patients/`).

### API Projet 2 :
Permet d’envoyer des données pour obtenir une prédiction de charges via l’endpoint `/predict`.

### Interface Projet 3 :
- **Récupération des données** : Un bouton permet de charger la liste des utilisateurs depuis l’API de Projet 1.
- **Prédiction individuelle** : Un formulaire interactif permet de saisir des caractéristiques (age, BMI, etc.) pour obtenir une prédiction de charges.
- **Prédiction en masse** : Possibilité d’importer un fichier CSV, d’effectuer des prédictions sur l’ensemble du fichier, de visualiser la distribution des charges prédites et d’exporter les résultats en CSV.
- **Journalisation** : Toutes les actions et erreurs sont enregistrées dans un fichier de logs (`projet3.log`) via Loguru.

## Contributions
Les contributions sont les bienvenues !

Pour contribuer :
- Forkez le dépôt.
- Créez une branche pour votre fonctionnalité ou correction (`git checkout -b feature/ma-feature`).
- Commitez vos modifications en suivant les conventions (PEP8, flake8, etc.).
- Ouvrez une pull request.

## Auteur

- **Mathieu Soussignan** : [Mathieu Soussignan](https://www.mathieu-soussignan.com/)

## Licence
Ce projet est sous licence MIT.