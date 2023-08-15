import requests
from django.template.defaulttags import csrf_token

url = "https://haveibeenpwned.com/unifiedsearch/pratishg@credy.in"

payload = "{\n\t\"Referrer\": \"https://haveibeenpwned.com/\"\n}"
headers = {
    '__cfduid':	'd6fbbc9c63a83dfe7d395377bb6b1fb301569951590',
    'content-type': "application/json"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)