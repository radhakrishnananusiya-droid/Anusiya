import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("Your Computer Name:",hostname)
print("Your Ip Address:",ip_address)

