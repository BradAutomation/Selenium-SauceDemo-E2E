from selenium.webdriver.common.by import By
# Importer la classe d'attente
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicLoadingPage:
    # Sélecteurs
    URL = "https://the-internet.herokuapp.com/dynamic_loading/1"
    START_BUTTON = (By.CSS_SELECTOR, "#start button")
    FINISH_TEXT = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Définir l'attente maximale ici

    def load(self):
        """Charge la page."""
        self.driver.get(self.URL)

    def start_loading(self):
        """Clique sur Start et utilise une attente explicite pour l'élément."""

        # 1. Cliquer sur le bouton Start
        self.driver.find_element(*self.START_BUTTON).click()

        # 2. Attendre Explicitement
        # Nous attendons la condition où l'élément FINISH_TEXT devient visible (en moins de 10s)
        self.wait.until(EC.visibility_of_element_located(self.FINISH_TEXT))

    def get_finish_message(self):
        """Récupère le texte une fois qu'il est visible."""
        # Puisque l'attente a été faite, la recherche d'élément est maintenant sûre.
        return self.driver.find_element(*self.FINISH_TEXT).text
