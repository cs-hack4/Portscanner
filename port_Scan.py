import socket

import pyfiglet

banner = pyfiglet.figlet_format("PORT SCANNER")
print(banner)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setdefauAF_INET,ttimeout(3)

port = input ("Enter Port:")
host = int(input("Enter IP:"))

def portscnner(port):
    if sock.connect_ex((port,host)):
        print("Port is open")
    else:
        print("Port is closed")

portscnner(port)
