# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def driver():
    """
    Fixture Selenium pour initialiser et fermer le navigateur Chrome en mode Headless.
    Contient les arguments de robustesse nécessaires pour l'exécution dans un conteneur Docker.
    """
    print("\n[SETUP] Démarrage du navigateur Chrome en mode Headless...")

    chrome_options = Options()

    # --- 1. CONFIGURATION CHROME POUR ENVIRONNEMENT CI/DOCKER ---

    # 1.1. Activation du mode Headless (sans interface graphique)
    chrome_options.add_argument("--headless=new")

    # 1.2. Arguments CRITIQUES pour les conteneurs Linux et les environnements CI
    # Ces arguments sont CRUCIAUX pour le bon fonctionnement dans un conteneur restreint.
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")

    # 1.3. Options et Préférences (Bonnes Pratiques)
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-features=PasswordManagerV2")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # Préférences pour BLOQUER le gestionnaire de mots de passe
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "webkit.webprefs.credential_management_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # CORRECTION FINALE : Chemin absolu du navigateur Chrome
    # Nous avons confirmé que le binaire est ici :
    chrome_options.binary_location = '/opt/google/chrome/google-chrome'

    # --- 2. CRÉATION DU DRIVER (Chemins confirmés) ---

    try:
        # CHEMIN CONFIRMÉ POUR LE DRIVER
        chrome_service = Service(executable_path='/usr/bin/chromedriver')

        driver = webdriver.Chrome(
            service=chrome_service,
            options=chrome_options
        )

    except Exception as e:
        print(f"Erreur lors de l'initialisation du driver: {e}")
        print("ACTION REQUISE : Vérifiez que 'docker run' utilise l'option '--ulimit nofile=32768'.")
        raise

    # Configuration initiale du driver
    driver.implicitly_wait(10)
    driver.set_window_size(1920, 1080)

    yield driver

    # [TEARDOWN] Fermeture du navigateur
    print("\n[TEARDOWN] Fermeture du navigateur...")
    driver.quit()