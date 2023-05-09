import socket
import requests
import json

UDP_IP = "0.0.0.0"
UDP_PORT = 8000
REST_URL = "http://localhost:5093/api/arrivals"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

print("Listening for UDP broadcast...")

while True:
    data, addr = sock.recvfrom(1024)
    print(data.decode())

    # Convert the JSON data to a Python dictionary
    json_data = json.loads(data.decode())

    # Post the JSON data to the REST service
    response = requests.post(REST_URL, json=json_data)

    if response.ok:
        print("Data sent to REST API successfully")
    else:
        print("Error sending data to REST API:", response.status_code)
