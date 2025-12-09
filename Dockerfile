# 1. Image de base : Utiliser l'image officielle Python avec la bonne version (3.9)
FROM python:3.9-slim

# 2. Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# 3. Installer Google Chrome et les outils nécessaires
# Cette partie simule l'installation de Chrome sur le serveur Linux
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable

# 4. Copier les dépendances Python et les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier le reste du projet (tests, pages, conftest, etc.) dans le conteneur
COPY . .

# 6. Commande par défaut : Définir la commande qui sera exécutée par défaut au démarrage du conteneur
CMD ["pytest", "--headless"]
