from pages.dynamic_loading_page import DynamicLoadingPage


def test_element_appears(driver):
    # Initialisation du Page Object
    dynamic_page = DynamicLoadingPage(driver)

    # Actions
    dynamic_page.load()
    dynamic_page.start_loading()  # Contient l'Attente Explicite

    # Assertion
    finish_text = dynamic_page.get_finish_message()

    # Le message attendu est "Hello World!"
    assert finish_text == "Hello World!"

    print("\n[Wait Test] Le texte 'Hello World!' est apparu avec succès.")
