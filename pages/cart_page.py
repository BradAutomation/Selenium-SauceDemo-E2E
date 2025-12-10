from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    # Sélecteurs
    # Liste des articles dans le panier (utilise un sélecteur CSS générique)
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")

    # Bouton pour démarrer le processus de paiement
    CHECKOUT_BUTTON = (By.ID, "checkout")

    # Nom du premier produit (pour la vérification)
    BACKPACK_ITEM_NAME = (By.ID, "item_4_title_link")

    # Sélecteur d'un élément crucial sur la page du panier (ex: le titre)
    TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    # Méthodes d'interaction

    def get_number_of_items(self):
        """Compte le nombre total d'articles affichés dans le panier."""

        # Attente critique : s'assurer que la page a chargé son contenu
        self.wait.until(EC.visibility_of_element_located(self.TITLE))
        # find_elements (au pluriel) retourne une liste d'éléments.
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def is_backpack_present(self):
        """Vérifie si le sac à dos est listé dans le panier."""
        # On peut simplement vérifier si l'élément spécifique est présent
        try:
            self.driver.find_element(*self.BACKPACK_ITEM_NAME)
            return True
        except:
            return False

    def go_to_checkout(self):
        """Clique sur le bouton Checkout pour passer aux informations."""
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
