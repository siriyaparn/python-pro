import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# Raises an HTTPError exception
response.raise_for_status()

data = response.json()
print(data)
# Output: {'timestamp': 1723827377, 'iss_position': {'latitude': '31.9354', 'longitude': '-53.7170'}, 'message': 'success'}
