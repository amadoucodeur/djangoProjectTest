# README

Ce projet est une application web Django qui gère des model3d et des badges associés à des utilisateurs. Le projet est divisé en deux répertoires principaux : back3dmodel et frontAPIs. Le répertoire back3dmodel contient le code source principal de l'application Django, tandis que le répertoire frontAPIs contient un client qui permet de tester les APIs de l'application.

Configuration de l'environnement de développement
Assurez-vous d'avoir Python installé sur votre système.

Créez un environnement virtuel (venv) pour isoler les dépendances du projet.

```bash
#Activez l'environnement virtuel.
python -m venv dgovenv
```

Sur Windows :

```bash
dgovenv\Scripts\activate
```

Sur macOS et Linux :

```bash
source dgovenv/bin/activate
```

Installez les dépendances requises en utilisant le fichier requirements.txt.

```bash
pip install -r requirements.txt
```

## Super utilisateur

Le super utilisateur par défaut pour l'application est :

Nom d'utilisateur : amadou
Mot de passe : amadou

## Structure du projet

Le projet est structuré de la manière suivante :

- back3dmodel : Le répertoire principal du projet Django.

    - app3dmodel : L'application Django principale qui gère les modèles 3D et les badges.

        1. models.py : Définition des modèles de données, y compris Model3d, Badge, et UserProfile.

        2. urls.py : Configuration des URL pour les vues de l'application.

        3. views.py : Implémentation des vues pour les modèles et les badges.

        4. settings.py : Configuration des paramètres Django de l'application.

        5. urls.py : Configuration des URL globales du projet.

- frontAPIs : Le répertoire contenant un client de test pour les APIs de l'application.

    - main.py : Un script Python qui vous permet de tester les APIs de l'application depuis la ligne de commande.

## Utilisation de l'application

1. Pour utiliser l'application, assurez-vous d'avoir configuré l'environnement virtuel et installé les dépendances.
2. Vous pouvez ensuite exécuter le serveur Django en utilisant la commande suivante depuis le répertoire back3dmodel :

    ```bash
    python manage.py runserver
    ```

3. L'application sera accessible à l'adresse http://localhost:8000/. Vous pouvez utiliser le super utilisateur par défaut pour accéder à l'interface d'administration.

N'hésitez pas à explorer le code source et à utiliser le client frontAPIs/main.py pour interagir avec les APIs de l'application.

### Auteur
Ce projet a été développé par Amadou Coulibaly

Pour toute question ou problème, n'hésitez pas à me contacter à [amadoucodeur@gmail.com](amadoucodeur@gmail.com)
