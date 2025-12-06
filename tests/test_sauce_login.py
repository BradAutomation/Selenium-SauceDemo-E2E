import pytest
from pages.login_page import SauceLoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage  # NOUVEAU

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


def test_complete_purchase_path(driver):  # Renommons la fonction pour refléter le parcours complet

    # Initialisation de TOUTES les Pages Objects nécessaires
    login_page = SauceLoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)  # NOUVEAU

    # --- 1. CONNEXION ET AJOUT (SETUP) ---
    login_page.load()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    # NOUVEAU: TENTER DE GÉRER LE POP-UP IMMÉDIATEMENT APRÈS LA CONNEXION
    login_page.handle_browser_popup()

    products_page.add_backpack_to_cart()
    products_page.add_bikelight_to_cart()

    # --- 2. VÉRIFICATION DU PANIER ---
    products_page.go_to_cart()

    # Assertion 1 : Le nombre d'articles affichés doit être 2
    assert cart_page.get_number_of_items() == 2
    print("\n[SauceDemo Test] Nombre d'articles dans le panier validé (2).")

    # Assertion 2 : Vérifier qu'un article spécifique est là
    assert cart_page.is_backpack_present() is True
    print("[SauceDemo Test] Le Sac à Dos est bien listé.")

    # --- 3. ACTION : ALLER AU CHECKOUT ---
    cart_page.go_to_checkout()
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"

    # --- 4. CHECKOUT STEP ONE : Saisir les informations ---
    checkout_page.fill_information("Jules", "Vern", "75001")  # Exemple de données
    checkout_page.continue_checkout()

    assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"
    print("[SauceDemo Test] Informations de livraison soumises.")

    # --- 5. CHECKOUT STEP TWO : Finalisation ---
    checkout_page.finish_purchase()

    # --- 6. ASSERTION FINALE : Vérifier la confirmation ---
    thank_you_message = checkout_page.get_thank_you_message()

    assert thank_you_message == "Thank you for your order!"
    print("[SauceDemo Test] Achat complet (E2E) validé avec succès!")

