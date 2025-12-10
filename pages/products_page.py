from selenium.webdriver.common.by import By
# Imports nécessaires pour l'Attente Explicite
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    # --- 1. SÉLECTEURS ---
    CART_ICON = (By.ID, "shopping_cart_container")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

    # Sac à Dos
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")  # L'élément qui apparaît après le clic

    # Lampe de Vélo
    ADD_TO_CART_BIKELIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    REMOVE_BIKELIGHT = (By.ID, "remove-sauce-labs-bike-light")  # L'élément qui apparaît après le clic

    # --- 2. CONSTRUCTEUR ---
    def __init__(self, driver):
        self.driver = driver
        # Correction de l'AttributeError: Initialisation de l'objet 'wait'
        self.wait = WebDriverWait(driver, 10)

        # --- 3. MÉTHODES D'INTERACTION ---

    def add_backpack_to_cart(self):
        """Ajoute le sac à dos au panier en forçant le clic via JavaScript."""

        # 1. Attendre que le bouton ADD soit présent et cliquable
        add_button = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BACKPACK))

        # 2. CORRECTION CRUCIALE : Exécuter le clic via JavaScript
        self.driver.execute_script("arguments[0].click();", add_button)

        # 3. Synchronisation : Attendre que le badge du panier soit créé dans le DOM
        self.wait.until(EC.presence_of_element_located(self.CART_BADGE))

        print("Article 'Sac à Dos' ajouté au panier par force JavaScript.")


    def add_bikelight_to_cart(self):
        """Ajoute le Bikelight au panier en forçant le clic via JavaScript."""

        # 1. Attendre que le bouton ADD soit présent et cliquable
        add_button = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BIKELIGHT))

        # 2. CORRECTION : Exécuter le clic via JavaScript
        self.driver.execute_script("arguments[0].click();", add_button)

        # 3. Synchronisation : Attendre que le badge du panier contienne un nombre > 1 (il est déjà là après le sac à dos)
        # L'attente de la présence du bouton REMOVE_BIKELIGHT est la plus directe
        self.wait.until(EC.presence_of_element_located(self.REMOVE_BIKELIGHT))

        print("Article 'Bikelight' ajouté au panier par force JavaScript.")

    def get_cart_count(self):
        """Retourne le nombre d'articles dans le panier."""
        return self.driver.find_element(*self.CART_BADGE).text

    def go_to_cart(self):
        """Clique sur l'icône du panier pour naviguer vers la page du panier."""
        self.driver.find_element(*self.CART_ICON).click()



