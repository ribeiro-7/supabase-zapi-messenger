import requests


ZAPI_BASE_URL = "https://api.z-api.io"
REQUEST_TIMEOUT = 30


def send_text(instance_id, instance_token, client_token, phone, message):
    url = (f"{ZAPI_BASE_URL}/instances/{instance_id}/token/{instance_token}/send-text")
    headers = {"Client-Token": client_token}
    payload = {
        "phone": phone,
        "message": message,
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()

    return response.json()
