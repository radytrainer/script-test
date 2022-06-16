import socket
import requests

hostname = socket.gethostname()
staticIp = socket.gethostbyname(hostname)

public = 'http://httpbin.org/ip'
publicIpAddress = requests.get(public).json()['origin']

print("Host name:" , hostname)
print("Static IP Address:" , staticIp)
print("Public IP address:" , publicIpAddress)