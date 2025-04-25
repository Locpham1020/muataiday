import requests

def send_to_airtable(token, base_id, table_name, payload):
    url = f"https://api.airtable.com/v0/{base_id}/{table_name}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    res = requests.post(url, headers=headers, json=payload)
    res.raise_for_status()
    return res.json()

def get_all_records(token, base_id, table_name):
    url = f"https://api.airtable.com/v0/{base_id}/{table_name}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return res.json().get("records", [])
