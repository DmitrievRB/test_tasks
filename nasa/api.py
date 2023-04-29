import requests
import json

earth_date = "2022-1-21"
api_key = "DEMO_KEY"
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
querystring = {"earth_date": earth_date,
            "api_key":api_key}
res = requests.request("get", url, timeout=3, params = querystring)
status = res.status_code
result = res.json()

# print(result)
print (status,result["photos"][1]["id"])



