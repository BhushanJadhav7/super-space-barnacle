import requests
import json
import pandas as pd

# URL of the API endpoint
url = "https://vegetablemarketprice.com/api/dataapi/market/maharashtra/daywisedata?date=2024-08-06"

# Headers for the HTTP request
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "cookie": "_ga=GA1.1.579592366.1719805178; JSESSIONID=94BC2263A4585B7B98973770D043973E; __gads=ID=d417311b4ca58bd6:T=1719805164:RT=1723005535:S=ALNI_MZBDVVGHlSQqR5k0P8vj4Ymc9foyA; __gpi=UID=00000e6d610639a0:T=1719805164:RT=1723005535:S=ALNI_MbOlZIJQSQMot2btmDNHhDbbUpTNw; __eoi=ID=5fb93107935acbae:T=1719805164:RT=1723005535:S=AA-Afjbak2cMxgawT7R_UvUzAL3n; _ga_2RYZG7Y4NC=GS1.1.1723005406.6.1.1723005422.0.0.0; FCNEC=%5B%5B%22AKsRol_kGpfj4tbq-JAcaePomD_rENfM7CoC2_i6HDJVYSw4cWOh7pQ9CXbipqMHb62O7np-PDjxheGEiTgZkJEE5FSrt9VaMjmBWfr2KCJxD3MS6AltfjtAvgrloBirs4JHC2h-PTsORX3xL8I2-nlxuCx-uNbtUg%3D%3D%22%5D%5D",
    "Referer": "https://vegetablemarketprice.com/market/maharashtra/today",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

# Fetch the data from the API
response = requests.get(url, headers=headers)
response.raise_for_status()  # Raise an error for bad responses

# Parse the JSON response
js_data = response.json()

# Extract and structure the data
arr_data = []
for api in js_data["data"]:
    veg_id = str(api["id"])
    veg_name = str(api["vegetablename"])
    whole_price = str(api["price"])
    retail_price = str(api["retailprice"])
    shoping_mall_price = str(api["shopingmallprice"])
    unit_val = str(api["units"])
    veg_image = str(api.get("vegetableimage", ""))  # Get the vegetable image if available

    new_js = {
        "veg_id": veg_id,
        "veg_name": veg_name,
        "whole_price": whole_price,
        "retail_price": retail_price,
        "shop_mall_price": shoping_mall_price,
        "unit_val": unit_val,
        "veg_image": veg_image
    }
    arr_data.append(new_js)

# Create a DataFrame from the structured data
df = pd.DataFrame(arr_data)

# Save the DataFrame to a CSV file
output_file = "vegetable_prices.csv"
df.to_csv(output_file, index=False)

print(f"Data successfully saved to {output_file}")
