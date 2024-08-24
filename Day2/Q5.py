import requests
#Url for the API
url = 'http://api.open-notify.org/iss-now.json'
#Get request
response = requests.get(url)
data=response.json()
#Print Latitude, Longitude,Timestamp
print("Latitude: ",data['iss_position']['latitude'])
print("Longitude: ",data['iss_position']['longitude'])
print("Timestamp: ",data['timestamp'])
