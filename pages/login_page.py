from selenium.webdriver.common.by import By


class LoginPage:
    # 1. Définir l'URL et les SÉLECTEURS de la page
    URL = "https://the-internet.herokuapp.com/login"

    # Utilisation de variables statiques pour les sélecteurs (meilleure pratique)
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".fa.fa-2x.fa-sign-in")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".flash")

    # 2. Le constructeur de la classe
    # Il reçoit l'objet 'driver' de la fixture Pytest
    def __init__(self, driver):
        self.driver = driver

    # 3. Les MÉTHODES d'interaction (ce que l'utilisateur fait)

    def load(self):
        """Charge la page de connexion."""
        self.driver.get(self.URL)

    def login(self, username, password):
        """Exécute la séquence complète de connexion."""

        # Trouver les éléments en utilisant les sélecteurs définis en haut
        username_field = self.driver.find_element(*self.USERNAME_INPUT)
        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)

        # Interagir
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

    def get_success_message_text(self):
        """Récupère le texte du message de succès après la connexion."""
        success_element = self.driver.find_element(*self.SUCCESS_MESSAGE)
        return success_element.text

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




