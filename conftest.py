import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# Si vous utilisiez ChromeDriverManager avant, assurez-vous de commenter
# ou de supprimer ces imports si vous ne l'utilisez plus.
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

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
    # --no-sandbox : Essentiel pour contourner les restrictions de sécurité du conteneur.
    # --disable-dev-shm-usage : Utile si --ipc=host ne suffit pas, mais --ipc=host est dans le docker run.
    # --user-data-dir : Redirige le cache utilisateur vers un dossier temporaire accessible (/tmp).
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

    # --- 2. CRÉATION DU DRIVER (Contournement de Selenium Manager) ---

    # Pour résoudre l'erreur de permission du cache de Selenium Manager,
    # nous spécifions explicitement le chemin du binaire ChromeDriver.
    # Assurez-vous que '/usr/bin/chromedriver' est le bon chemin dans votre image Docker.
    try:
        chrome_service = Service(executable_path='/usr/local/bin/chromedriver')

        driver = webdriver.Chrome(
            service=chrome_service,
            options=chrome_options
        )

    except Exception as e:
        # Permet de déboguer si le chemin du driver est incorrect
        print(f"Erreur lors de l'initialisation du driver: {e}")
        print("Vérifiez que ChromeDriver est installé à '/usr/bin/chromedriver' dans le conteneur.")
        raise

    # Configuration initiale du driver
    driver.implicitly_wait(10)
    driver.set_window_size(1920, 1080)

    yield driver

    # [TEARDOWN] Fermeture du navigateur
    print("\n[TEARDOWN] Fermeture du navigateur...")
    driver.quit()

