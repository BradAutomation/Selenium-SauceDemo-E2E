import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


@pytest.fixture(scope="session")
def driver():
    print("\n[SETUP] Démarrage du navigateur Chrome en mode Headless...")

    chrome_options = Options()

    # --- 1. ACTIVATION DU MODE HEADLESS ---
    # Cela garantit que le navigateur s'exécute en arrière-plan sans interface graphique
    # et supprime la plupart des interférences du navigateur.
    chrome_options.add_argument("--headless=new")

    # --- 2. OPTIONS ET PRÉFÉRENCES (BONNES PRATIQUES) ---
    # Option anti-détection (même si souvent ignorée en headless)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # Préférences pour BLOQUER le gestionnaire de mots de passe, juste au cas où
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "webkit.webprefs.credential_management_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Autres arguments de robustesse
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-features=PasswordManagerV2")

    # 3. Création du driver avec toutes les options configurées
    driver = webdriver.Chrome(
        # service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )

    # Attente implicite globale
    driver.implicitly_wait(20)

    # Le 'yield' renvoie l'objet driver au test
    yield driver

    # 4. TEARDOWN : Fermeture du navigateur
    print("\n[TEARDOWN] Fermeture du navigateur...")
    time.sleep(1)
    driver.quit()


