import requests
import pandas as pd
import time

# Function to get the current location of the ISS
def get_iss_location():
    url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)
    data = response.json()
    return {
        'timestamp': data['timestamp'],
        'latitude': data['iss_position']['latitude'],
        'longitude': data['iss_position']['longitude']
    }

# List to store the ISS location data
iss_data = []

# Collecting data 100 times with a 10-second interval
for _ in range(100):
    iss_data.append(get_iss_location())
    time.sleep(10)

# Creating a DataFrame from the collected data
df = pd.DataFrame(iss_data)

# Saving the DataFrame to a CSV file
df.to_csv('iss_location.csv', index=False)

print("CSV file 'iss_location.csv' with a minimum of 100 records has been created")

# Reading the CSV file into a DataFrame
df = pd.read_csv('iss_location.csv')

# Printing the DataFrame
print(df)
