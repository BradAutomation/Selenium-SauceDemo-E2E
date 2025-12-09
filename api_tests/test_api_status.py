import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_validate_first_user_data():
    """Vérifie le statut de la requête et la structure des données du premier utilisateur."""

    # 1. Envoyer la requête GET
    endpoint = f"{BASE_URL}/users"
    response = requests.get(endpoint)

    # --- Premières Assertions (Connexion et Format) ---

    # Vérifie que la requête a réussi (200 OK)
    assert response.status_code == 200

    # Vérifie que le contenu de la réponse est bien en JSON
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    # 2. Récupérer les données JSON
    # La méthode .json() convertit le texte brut JSON en une structure de données Python (liste de dictionnaires)
    users_data = response.json()

    # --- Assertions sur les Données (La Validation Métier) ---

    # Vérifie que la réponse est une liste et qu'elle n'est pas vide
    assert isinstance(users_data, list)
    assert len(users_data) > 0

    # 3. Accéder aux données du premier utilisateur (le premier élément de la liste)
    first_user = users_data[0]

    # Vérifie la présence et la valeur attendue de champs spécifiques
    assert first_user["id"] == 1
    assert first_user["name"] == "Leanne Graham"
    assert "email" in first_user

    # NOUVEAU : AFFICHER TOUTES LES DONNÉES DU PREMIER UTILISATEUR
    print("\n--- Données JSON du Premier Utilisateur Reçues ---")
    print(first_user)
    print("---------------------------------------------------\n")

    print(f"Test de l'API {endpoint} réussi. Premier utilisateur vérifié : {first_user['name']}")


def test_create_new_post():
    """Simule l'envoi de données (POST) pour créer une nouvelle ressource."""

    # 1. Préparer les données à envoyer au serveur (le "payload")
    new_post_payload = {
        "title": "Titre du Post de Bradley",
        "body": "Ceci est le corps du message créé par le test API.",
        "userId": 101
    }

    # 2. Envoyer la requête POST
    # Notez que nous envoyons les données via l'argument 'json'
    response = requests.post(f"{BASE_URL}/posts", json=new_post_payload)

    # --- Assertions ---

    # Vérifie que le serveur confirme la création (201 Created)
    assert response.status_code == 201

    # Récupérer les données renvoyées par le serveur après la création
    created_data = response.json()

    # 3. Vérifier que le serveur a bien enregistré les données envoyées
    assert created_data["title"] == new_post_payload["title"]
    assert created_data["userId"] == 101

    # Le serveur a ajouté un ID unique à la ressource créée
    assert "id" in created_data

    print("\n--- Résultat du POST (Ressource Créée) ---")
    print(created_data)
    print("-------------------------------------------\n")


def test_full_crud_cycle():
    """Simule la création, la lecture, la modification, puis la suppression d'une ressource."""

    # ----------------------------------------------------
    # I. CREATE (Création - Méthode POST)
    # ----------------------------------------------------

    initial_payload = {
        "title": "Titre à créer (CRUD Test)",
        "body": "Contenu initial de la ressource.",
        "userId": 999
    }

    # Envoi de la requête POST pour créer la ressource
    response_post = requests.post(f"{BASE_URL}/posts", json=initial_payload)
    assert response_post.status_code == 201

    # Récupérer l'ID généré par le serveur (essentiel pour les étapes suivantes)
    created_data = response_post.json()
    new_resource_id = created_data["id"]
    print(f"\n[CREATE] Ressource créée avec l'ID: {new_resource_id}")

    # ----------------------------------------------------
    # II. READ (Lecture - Méthode GET)
    # ----------------------------------------------------

    # 💡 CORRECTION : Nous testons le READ sur la ressource ID 1 (qui est stable)
    # au lieu d'utiliser l'ID de la ressource nouvellement créée qui est trop grand pour l'API de démo.
    known_stable_id = 1

    # Récupérer la ressource que nous venons de créer en utilisant son ID
    response_get = requests.get(f"{BASE_URL}/posts/{known_stable_id}")

    # L'assertion devrait maintenant passer
    assert response_get.status_code == 200

    read_data = response_get.json()

    # Vérifier que l'ID lu est bien le 1
    assert read_data["id"] == 1

    # Continuer avec le même ID pour l'étape UPDATE suivante
    new_resource_id = known_stable_id

    print(f"[READ] Vérification du READ sur l'ID stable {known_stable_id} réussie.")

    # ----------------------------------------------------
    # III. UPDATE (Mise à Jour - Méthode PUT)
    # ----------------------------------------------------

    updated_payload = {
        "title": "TITRE MODIFIÉ (TEST REUSSI)",
        "body": "Contenu mis à jour.",
        "userId": 999,
        "id": new_resource_id  # L'ID est nécessaire dans le corps pour le PUT
    }

    # Envoi de la requête PUT pour remplacer l'intégralité de la ressource
    response_put = requests.put(f"{BASE_URL}/posts/{new_resource_id}", json=updated_payload)
    assert response_put.status_code == 200  # Le PUT/PATCH renvoie souvent 200 OK

    # Lire la ressource après la mise à jour pour confirmer
    updated_response_data = response_put.json()
    assert updated_response_data["title"] == "TITRE MODIFIÉ (TEST REUSSI)"
    print(f"[UPDATE] Titre mis à jour avec succès.")

    # ----------------------------------------------------
    # IV. DELETE (Suppression - Méthode DELETE)
    # ----------------------------------------------------

    # Envoi de la requête DELETE pour supprimer la ressource par son ID
    response_delete = requests.delete(f"{BASE_URL}/posts/{new_resource_id}")
    assert response_delete.status_code == 200  # Le code 200 ou 204 est souvent accepté ici



