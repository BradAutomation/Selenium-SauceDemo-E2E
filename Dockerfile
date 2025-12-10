# 1. Image de base : Utiliser une image de Selenium qui a Chrome et toutes les dépendances
# Cela évite de déboguer l'installation de Chrome et de toutes ses dépendances.
# Nous utilisons l'image Chrome stable, basée sur Python 3.9
FROM selenium/standalone-chrome:latest

# 2. Définir le répertoire de travail
WORKDIR /app

# 3. Installer Python
# Nous devons devenir root pour pouvoir utiliser apt-get
USER root
RUN apt-get update && apt-get install -y python3 python3-pip

# Revenir à l'utilisateur par défaut (souvent 'seluser') pour des raisons de sécurité
# Nous devons le faire car les étapes suivantes doivent fonctionner sous cet utilisateur
USER seluser

# 4. Copier les dépendances Python et les installer
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# 5. Copier le reste du projet (tests, pages, conftest, etc.)
COPY . .

# NOUVEAU : Récupérer le nom de l'utilisateur par défaut (souvent 'seluser' ou 'chrome')
# Pour changer le propriétaire des fichiers, nous devons revenir en root
USER root

# CORRECTION : Changer les permissions pour que l'utilisateur non-root par défaut (ID 1000)
# puisse écrire dans le dossier /app/. Cela contourne l'erreur `seluser` inconnu.
RUN chown -R 1000:1000 /app

# Revenir à l'utilisateur non-root (celui qui exécute Chrome/Selenium) pour des raisons de sécurité
USER 1000

# 6. Commande par défaut : Lancer Pytest.
CMD ["pytest"]