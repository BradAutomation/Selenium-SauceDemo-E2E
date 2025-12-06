from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    # Sélecteurs (vérifiez-les avec l'Inspecteur !)
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")

    # Sélecteur de la page de confirmation finale
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_information(self, first_name, last_name, postal_code):
        """Remplir les champs de la première étape du checkout."""

        # Trouver les éléments (pour ne pas répéter la recherche)
        first_name_el = self.driver.find_element(*self.FIRST_NAME_INPUT)
        last_name_el = self.driver.find_element(*self.LAST_NAME_INPUT)
        postal_code_el = self.driver.find_element(*self.POSTAL_CODE_INPUT)

        # 1. Nettoyer les champs (BONNE PRATIQUE)
        first_name_el.clear()
        last_name_el.clear()
        postal_code_el.clear()

        # 2. Saisir les nouvelles valeurs
        first_name_el.send_keys(first_name)
        last_name_el.send_keys(last_name)
        postal_code_el.send_keys(postal_code)

    def continue_checkout(self):
        """Passer à la page de confirmation."""
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def finish_purchase(self):
        """Finaliser l'achat."""
        # Utiliser une attente explicite pour s'assurer que la page de confirmation est chargée
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON))
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def get_thank_you_message(self):
        """Récupère le message de succès final."""
        # Utiliser une attente explicite car la page change
        self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER))
        return self.driver.find_element(*self.COMPLETE_HEADER).text

