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

# NOUVEAU : Corriger les permissions d'écriture pour l'utilisateur non-root (seluser)
# seluser est l'utilisateur par défaut dans l'image Selenium
RUN chown -R seluser:seluser /app

# 6. Commande par défaut : Lancer Pytest.
CMD ["pytest"]