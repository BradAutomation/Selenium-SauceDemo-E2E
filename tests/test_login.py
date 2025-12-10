import pytest
from pages.login_page import LoginPage  # Utilise la classe LoginPage corrigée

# Les identifiants de démo pour Sauce Demo
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"

# Le driver est toujours fourni par la fixture 'driver' dans conftest.py
def test_login_success_pom(driver):
    # 1. INITIALISATION : Créer une instance de la Page Object
    login_page = LoginPage(driver)

    # 2. ACTIONS : Utiliser les méthodes de la Page Object
    login_page.load()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    # 3. ASSERTION : Valider le résultat (le cœur du test)

    # Valider la redirection vers la page d'inventaire
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    # Vérifier un élément sur la page de succès (par exemple, le titre 'Products')
    # Vous devrez ajouter une méthode dans login_page.py pour valider un élément
    # Pour l'instant, on se contente de l'URL pour la simplicité du test.

    print("\n[POM Test] Connexion Sauce Demo réussie (via URL).")


def test_login_failure_pom(driver):
    login_page = LoginPage(driver)

    # Actions avec identifiants incorrects
    login_page.load()
    login_page.login("locked_out_user", VALID_PASSWORD) # locked_out_user échoue la connexion

    # Assertion : vérifier l'échec
    failure_text = login_page.get_error_message() # Cette méthode est déjà dans votre PO

    assert "Epic sadface: Sorry, this user has been locked out." in failure_text
    print("\n[POM Test] Échec de connexion Sauce Demo validé.")

