import requests

url = 'http://localhost:5000/predict'

post_response = requests.post(url, json={'features': [1.0, 2.0, 3.0]})
print('POST response:', post_response.json())

# its the same as http://localhost:5000/predict?features=1.1,2.0,3.0
get_response = requests.get(url, params={'features': [1.1, 2.0, 3.0]})
print('GET response:', get_response.json())
