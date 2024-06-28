import requests

url="http://api.open-notify.org/iss-now.json"

response = requests.get(url)
if response.status_code==200:
    print("Response")
    print(response.json())
else:
    print("Error")
