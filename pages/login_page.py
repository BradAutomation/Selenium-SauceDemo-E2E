from selenium.webdriver.common.by import By

###############################################
###############################################
###############################################
###############################################

class SauceLoginPage:
    URL = "https://www.saucedemo.com/"

    # Sélecteurs (vérifiez ces ID avec l'Inspecteur!)
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    # Message d'erreur (si la connexion échoue)
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container.error")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        """Charge la page de connexion."""
        self.driver.get(self.URL)

    def login(self, username, password):
        """Exécute la séquence de connexion."""

        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        """Récupère le texte du message d'erreur en cas d'échec."""
        error_element = self.driver.find_element(*self.ERROR_MESSAGE)
        return error_element.text

    def handle_browser_popup(self):
        """Tente de cliquer sur le bouton 'OK' d'une fenêtre modale du navigateur."""
        try:
            # Cible le bouton 'OK' du pop-up Chrome (ce sélecteur est une tentative)
            ok_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            ok_button.click()
            print("Pop-up Chrome géré (clic sur OK).")
        except Exception:
            # Si le bouton n'est pas trouvé (le pop-up n'est pas là), on ignore l'exception
            pass




