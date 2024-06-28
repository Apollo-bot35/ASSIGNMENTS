import requests
import json

url = "http://api.open-notify.org/iss-now.json"

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

data = requests.get(url,headers=header)
print(data)

js_data = json.loads(data.text)

print(js_data["iss_position"])
print(js_data["timestamp"])
