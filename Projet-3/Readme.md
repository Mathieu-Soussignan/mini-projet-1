# Projet 3 – Orchestration et Journalisation

Ce projet a pour objectif d’orchestrer les appels aux APIs des Projets 1 et 2, tout en offrant une interface utilisateur (via **Streamlit**) et une journalisation complète (via **loguru**).

## Sommaire
1. [Architecture Générale](#architecture-générale)
2. [Prérequis](#prérequis)
3. [Installation et Lancement](#installation-et-lancement)
4. [Utilisation](#utilisation)
5. [Docker Compose](#docker-compose)
6. [Journalisation](#journalisation)
7. [Contribuer](#contribuer)

---

## Architecture Générale

- **Projet 1** : API de gestion des coûts médicaux (patients, utilisateurs, etc.).
- **Projet 2** : API de prédiction des charges (modèle IA).
- **Projet 3** : Application Streamlit qui orchestre les appels aux deux APIs et journalise les événements.

Le Projet 3 permet :
- De récupérer des données depuis l’API du Projet 1.
- D’envoyer des requêtes de prédiction à l’API du Projet 2.
- D’afficher les résultats dans une interface web (Streamlit).
- De journaliser toutes les actions via loguru.

---

## Prérequis

- **Python 3.9+** (si vous exécutez localement hors Docker)
- **Pip** ou un gestionnaire de dépendances
- **Docker** et **Docker Compose** (si vous utilisez la solution multi-container)

---

## Installation et Lancement

### 1. En local (hors Docker)

1. Clonez ce dépôt et placez-vous dans le dossier `Projet-3`.
2. Créez et activez un environnement virtuel (optionnel).
3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
4. Lancez l’application Streamlit :
    ```bash
    streamlit run app.py --server.port=8501
5. Accédez à http://localhost:8501 pour voir l’interface.

Note : Les appels vers Projet 1 et Projet 2 doivent pointer vers les URLs correctes (par exemple, localhost:8001 ou localhost:8002) si vous exécutez ces projets en local.

### 2. Via Docker Compose

1. Assurez-vous d'avoir un fichier docker-compose.yml à la racine du projet global.
2. Dans ce fichier, sont définis les services api-proj1, api-proj2 et api-proj3.
3. Lancez le docker-compose :
   ```bash
   docker-compose up --build
4. Accédez à http://localhost:8501 pour voir l’interface.

Attention : Dans ce mode, le code du Projet 3 appelle les services via http://api-proj1:8000 et http://api-proj2:8000 (noms de service Docker Compose).

---

## Utilisation

- Récupérer la liste des utilisateurs :
Un bouton dans l’interface Streamlit appelle l’API du Projet 1 (ex. /utilisateurs/) pour afficher les données.

- Effectuer une prédiction :
Renseignez les champs (age, bmi, children, etc.) et cliquez sur “Prédire”. L’interface appelle l’API Projet 2 (endpoint /predict) et affiche la valeur de predicted_charges.


---

## Docker Compose

Le docker-compose.yml contient les services suivants :

- api-proj1 : API du Projet 1
- api-proj2 : API du Projet 2
- api-proj3 : API du Projet 3

Chaque service est défini dans un fichier docker-compose.yml dans le dossier correspondant (Projet-1, Projet-2, Projet-3).

Les services sont définis avec les ports 8000 et 8501 (http et streamlit) et le volume /app (dossier de l’application).

---

## Journalisation

Le fichier modules/logger.py configure loguru pour journaliser les actions dans un fichier projet3.log. Vous verrez par exemple :

- GET utilisateurs successful lorsque la récupération des utilisateurs (Projet 1) se déroule bien.
- POST predict successful lorsqu’une prédiction (Projet 2) aboutit.
En cas d’erreur, des messages de niveau ERROR sont également enregistrés, facilitant le débogage.

---

Contribution

1. Forkez ce dépôt.

2. Créez une branche pour votre fonctionnalité ou correction (git checkout -b feature/ma-feature).

3. Commitez et push vos modifications.

4. Ouvrez une pull request.

Merci de suivre les conventions de code (flake8, PEP8) et d’ajouter des tests si possible.

---

Contact : Pour toute question, vous pouvez contacter **Mathieu Soussignan**.