import requests

with open("openaq.key") as f:
    api_key = f.read().strip()

url = "https://api.openaq.org/v3/locations/8415"
headers = {"X-API-Key": api_key}

response = requests.get(url, headers=headers, timeout=30)

print("Status code:", response.status_code)
print(response.text[:1500])