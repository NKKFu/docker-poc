import requests
from datetime import datetime

results = {}

while True:
    response = requests.get("http://localhost/app2")
    results[response.status_code] = results.get(response.status_code, 0) + 1
    print(f"[app2][{datetime.now()}] {results}")
