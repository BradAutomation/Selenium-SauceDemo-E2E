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
        """Ajoute le sac à dos au panier en assurant la synchronisation via le badge."""

        # 1. Attendre que le bouton ADD soit cliquable ET cliquer
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BACKPACK)).click()

        # 2. Synchronisation CRITIQUE : Attendre que le badge du panier devienne visible
        # C'est la méthode de vérification la plus robuste.
        self.wait.until(EC.visibility_of_element_located(self.CART_BADGE))

        # 3. Optionnel : Attendre que le bouton REMOVE apparaisse (pour la forme)
        # self.wait.until(EC.element_to_be_clickable(self.REMOVE_BACKPACK)) # Ligne qui échouait

        print("Article 'Sac à Dos' ajouté au panier et confirmation reçue via le badge.")

    def add_bikelight_to_cart(self):
        """Ajoute la lampe de vélo au panier en assurant la synchronisation."""

        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BIKELIGHT))

        self.driver.find_element(*self.ADD_TO_CART_BIKELIGHT).click()

        # Attente pour la confirmation de l'ajout
        self.wait.until(EC.visibility_of_element_located(self.REMOVE_BIKELIGHT))
        print("Article 'Lampe de Vélo' ajouté au panier et confirmation reçue.")

    def get_cart_count(self):
        """Retourne le nombre d'articles dans le panier."""
        return self.driver.find_element(*self.CART_BADGE).text

    def go_to_cart(self):
        """Clique sur l'icône du panier pour naviguer vers la page du panier."""
        self.driver.find_element(*self.CART_ICON).click()



