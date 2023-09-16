import requests


def make_request(self_, endpoint: str, params=None):
    response = requests.get(f"{self_.BASE_URL}/{endpoint}", params=params)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
