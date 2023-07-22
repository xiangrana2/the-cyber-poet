import requests

def setup_wordpress(api_url, username, password):
    # You might need to change this to suit your authentication method
    response = requests.post(f"{api_url}/jwt-auth/v1/token", data={"username": username, "password": password})
    response.raise_for_status()
    return response.json()["token"]

def create_post(api_url, auth_token, post_data):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(f"{api_url}/wp/v2/posts", headers=headers, json=post_data)
    response.raise_for_status()
    return response.json()