import requests
import os

UNLEASH_API_URL = os.getenv("UNLEASH_API_URL")
UNLEASH_API_KEY = os.getenv("UNLEASH_API_KEY")

def is_feature_enabled(feature_name, user_id=None):
    headers = {"Authorization": UNLEASH_API_KEY}
    params = {"userId": user_id} if user_id else {}

    response = requests.get(f"{UNLEASH_API_URL}/api/client/features/{feature_name}", headers=headers, params=params)
    if response.status_code == 200:
        feature_data = response.json()
        return feature_data.get("enabled", False)
    return False
