import pytest
from pages.login_page import LoginPage  # Importer la classe Page Object

# Les identifiants de démo pour la connexion réussie
VALID_USERNAME = "tomsmith"
VALID_PASSWORD = "SuperSecretPassword!"


# Le driver est toujours fourni par la fixture 'driver' dans conftest.py
def test_login_success_pom(driver):
    # 1. INITIALISATION : Créer une instance de la Page Object
    login_page = LoginPage(driver)

    # 2. ACTIONS : Utiliser les méthodes de la Page Object
    login_page.load()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    # 3. ASSERTION : Valider le résultat (le cœur du test)

    # Récupérer le message de succès via la Page Object
    success_text = login_page.get_success_message_text()

    # Valider le texte du message
    assert "You logged into a secure area!" in success_text

    # Valider la redirection (URL)
    assert driver.current_url == "https://the-internet.herokuapp.com/secure"

    print("\n[POM Test] Connexion réussie et message validé.")


def test_login_failure_pom(driver):
    login_page = LoginPage(driver)

    # Actions avec identifiants incorrects
    login_page.load()
    login_page.login("invalid_user", "wrong_password")

    # Assertion : vérifier l'échec (le message contient "Your username is invalid")
    failure_text = login_page.get_success_message_text()  # Le sélecteur .flash fonctionne aussi pour l'échec

    assert "Your username is invalid!" in failure_text
    print("\n[POM Test] Échec de connexion validé.")

