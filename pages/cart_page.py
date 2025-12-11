# pages/cart_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Page Object Model pour la page du Panier (Cart Page)
    """

    # --- SÉLECTEURS ---

    # SÉLECTEUR CORRIGÉ pour compter les articles :
    # Le conteneur de chaque article dans le panier sur le site Sauce Demo
    CART_ITEM_CONTAINER = (By.CLASS_NAME, 'cart_item')

    # Bouton pour Checkout
    CHECKOUT_BUTTON = (By.ID, 'checkout')

    # Élément de l'article spécifique (pour vérification)
    BACKPACK_ITEM_NAME = (By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']")

    # --- CONSTRUCTEUR ---

    def __init__(self, driver):
        self.driver = driver

    # --- ACTIONS ---

    def is_backpack_present(self):
        """
        Vérifie si le sac à dos est listé dans le panier.
        """
        try:
            # On peut simplement vérifier si l'élément spécifique est présent
            self.driver.find_element(*self.BACKPACK_ITEM_NAME)
            return True
        except:
            return False

    def get_number_of_items(self):
        """
        Retourne le nombre d'articles actuellement visibles dans le panier.
        """
        # Attendre que les éléments du panier soient présents avant de les compter
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.CART_ITEM_CONTAINER)
            )

            # Compter tous les conteneurs d'articles trouvés
            items = self.driver.find_elements(*self.CART_ITEM_CONTAINER)
            print(f"DEBUG: {len(items)} articles trouvés dans le panier.")
            return len(items)

        except:
            # Si l'attente échoue, il est probable qu'il n'y ait aucun article
            return 0

    def go_to_checkout(self):
        """
        Clique sur le bouton Checkout pour passer aux informations.
        """
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()