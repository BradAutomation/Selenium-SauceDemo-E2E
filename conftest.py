# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# ... le reste des imports

@pytest.fixture(scope="session")
def driver():
    # ... (Début du code inchangé)

    chrome_options = Options()

    # --- 1. CONFIGURATION CHROME POUR ENVIRONNEMENT CI/DOCKER ---

    # 1.1. Activation du mode Headless (sans interface graphique)
    chrome_options.add_argument("--headless=new")

    # 1.2. Arguments CRITIQUES pour les conteneurs Linux et les environnements CI
    # Ces arguments sont CRUCIAUX pour le bon fonctionnement dans un conteneur restreint.
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # NOUVEL ARGUMENT CRITIQUE : Désactive le mécanisme de sandbox le plus restrictif
    # Ceci est SOUVENT la cause des plantages soudains dans les conteneurs CI.
    chrome_options.add_argument("--disable-gpu")

    # Ajoutez également cette ligne pour les environnements CI particulièrement restreints
    chrome_options.add_argument("--disable-setuid-sandbox")

    chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")

    # ... (Le reste du code de chrome_options est inchangé)

    # CORRECTION FINALE : Chemin absolu du navigateur Chrome
    chrome_options.binary_location = '/opt/google/chrome/google-chrome'

    # ... (Le reste du code de création du driver est inchangé)