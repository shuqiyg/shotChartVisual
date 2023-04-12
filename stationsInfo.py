import requests
from dotenv import load_dotenv
import os, json

load_dotenv()

apiKey = os.environ.get('govApiKey')
print(apiKey)
url = f"https://developer.nrel.gov/api/alt-fuel-stations/v1.json?limit=2&api_key={apiKey}"
print(url)
response = requests.get(url)

if response.status_code == 200:
    content = response.content
    # content = json.dumps(content)
    print(type(content))
    print(type(content.decode()))
    print(json.loads(content.decode())['fuel_stations'][1])

else:
    print("Error:", response.status_code)
