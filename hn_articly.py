import requests #import requests module
import json #import json module
#make an API call, store the response
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

#explore the structure of the data
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)