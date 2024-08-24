import requests
#Url for the API
url = 'http://api.open-notify.org/iss-now.json'
#Get request
response = requests.get(url)
#Json response
print(response.json())