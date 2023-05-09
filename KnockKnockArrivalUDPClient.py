from datetime import date
import datetime
import socket
import json
import time
import pytz

cet = pytz.timezone('CET')

UDP_IP = "255.255.255.255"
UDP_PORT = 8000

ArrivalTime = datetime.datetime.now(cet).strftime("%Y-%m-%dT%H:%M:%SZ")

QrCode = 23523542

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:

    data = {
        "arrivalTime": ArrivalTime,
        "qrCode": QrCode
    }
    json_data = json.dumps(data)

    sock.sendto(json_data.encode(), (UDP_IP, UDP_PORT))

    time.sleep(10.0)