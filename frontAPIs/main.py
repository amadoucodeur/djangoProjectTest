import requests

base_url = "http://127.0.0.1:8000/api/"

# Fonction pour afficher la réponse de la requête
def afficher_reponse(response):
    print("Statut de la réponse:", response.status_code)
    if response.status_code == 200:
        print("Contenu de la réponse:")
        print(response.json())
    else:
        print("Erreur:", response.text)

if __name__ == "__main__":
    # GET à la liste des badges
    url = base_url + "models/"
    response = requests.get(url)
    afficher_reponse(response)

    # GET à un modèle 3D spécifique par ID
    model_id = 3  
    url = base_url + f"models/{model_id}/"
    response = requests.get(url)
    afficher_reponse(response)

    # GET à la liste des badges
    url = base_url + "badges/"
    response = requests.get(url)
    afficher_reponse(response)

    # GET à un badge spécifique par ID
    badge_id = 1  
    url = base_url + f"badges/{badge_id}/"
    response = requests.get(url)
    afficher_reponse(response)

    # GET à la liste des profils d'utilisateurs
    url = base_url + "profiles/"
    response = requests.get(url)
    afficher_reponse(response)

    # GET à un profil utilisateur spécifique par ID
    user_profile_id = 2  
    url = base_url + f"profiles/{user_profile_id}/"
    response = requests.get(url)
    afficher_reponse(response)
