# 🚀 Projet d'Automatisation QA : Parcours d'Achat E2E

## ✅ Statut de l'Intégration Continue (CI)

[![Python Pytest CI](https://github.com/BradAutomation/Selenium-SauceDemo-E2E/actions/workflows/ci_e2e_tests.yml/badge.svg)](https://github.com/BradAutomation/Selenium-SauceDemo-E2E/actions/workflows/ci_e2e_tests.yml)

---
## 🎯 Objectif du Projet

Ce projet implémente une solution d'automatisation de tests End-to-End (E2E) pour le site de démonstration [Sauce Demo](https://www.saucedemo.com/).

Le but principal est de **valider la stabilité et la complétude du parcours d'achat critique** dans un environnement d'Intégration Continue (CI).

### 🛠️ Technologies Utilisées

* **Langage :** Python 3.9+
* **Framework de Test :** Pytest
* **Automatisation :** Selenium WebDriver
* **Architecture :** Page Object Model (POM)
* **CI/CD :** GitHub Actions (pour l'exécution automatique des tests)

---
## 📝 Scénario de Test Couvert

**Titre du Test :** `test_complete_purchase_path`

Ce scénario couvre le cycle de vie complet d'un utilisateur réussissant son achat, du début à la fin :

1.  Connexion réussie avec l'utilisateur standard.
2.  Ajout de deux articles au panier (`Sauce Labs Backpack` et `Bike Light`).
3.  Vérification de l'icône du panier (compteur `2`).
4.  Validation de la présence des articles sur la page du Panier.
5.  Passage à la caisse (Checkout) et saisie des informations de livraison.
6.  Confirmation et finalisation de la commande.
7.  Assertion finale du message de succès ("Checkout: Complete!").

---
## 🧠 Leçons Apprises et Stabilité du Code

Ce projet a mis en œuvre plusieurs pratiques avancées pour garantir la stabilité, notamment lors de l'exécution Headless sur le serveur CI :

* **Synchronisation Robuste :** Utilisation systématique des **Attentes Explicites (`WebDriverWait`)** après chaque action critique (ex: attendre l'apparition du bouton "Remove" pour confirmer l'ajout au panier).
* **Contournement des Interférences :** Configuration du driver Chrome en mode **Headless** dans `conftest.py` pour éliminer les pop-ups de sécurité du navigateur qui bloquaient le test.
* **Fiabilité du Test :** Remplacement des assertions fragiles (ex: vérification des messages éphémères) par des validations d'état fiables (ex: vérification de l'URL pour la confirmation de connexion).

---
## ▶️ Comment Exécuter le Test Localement

1.  **Cloner le Dépôt :**
    ```bash
    git clone [https://github.com/BradAutomation/Selenium-SauceDemo-E2E.git](https://github.com/BradAutomation/Selenium-SauceDemo-E2E.git)
    cd Selenium-SauceDemo-E2E
    ```
2.  **Installer les Dépendances :**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Lancer le Test E2E :**
    ```bash
    pytest tests/test_sauce_login.py
    ```
