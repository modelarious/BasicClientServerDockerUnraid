# client that sends a message to the server at 192.168.1.75:5000/echo and checks it responded with the same message
import requests

url = 'http://192.168.1.75:5000/echo'
data = {'message': 'Hello from client!'}

response = requests.post(url, json=data)

if response.status_code != 200:
    print(f"ERROR: {response.status_code}")
else:
    response_data = response.json()
    if response_data['message'] != data['message']:
        print(f"ERROR: Server responded with {response_data['message']} instead of {data['message']}")
    else:
        print(f"SUCCESS: Server responded with {response_data['message']}")

