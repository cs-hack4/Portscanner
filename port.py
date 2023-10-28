import pyfiglet
import sys
import socket
from datetime import datetime

banner = pyfiglet.figlet_format("PORT SCANNER")
print(banner)

# Defining a target
if len(sys.argv) == 2:
     
    # translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")
 
# add banner 

print("-"* 50)
print("Scanning Terget: " + target)
print ("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:
    for port in range(1,65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        socket.setdefaulttimeout(1)

        result = sock.connect_ex((target,port))
        if result == 0:
            print("port {} is open".formet(port))
            sock.close()

except keybordinterrupt:
    print("\n Exiting program !!!")
    sys.exit()

except socket.gaierror:
    print("\n Host name could not be resolved !!!")
    sys.exit()

except socket.error:
    print("\ Server not responding !!!")
    sys.exit()

