#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg
import socket

# decoration
print(stylize("\n---- | Get hostname and host ip address | ----\n", fg("red")))

# function
def host_ip():
   try:
      hname = socket.gethostname()
      hip = socket.gethostbyname(hname)
      return hname, hip
   except:
      return -1

# output
result = host_ip()

if result != -1:
    print(f"The hostname is: {result[0]}\nThe IP Address is: {result[1]}\n")
else:
    print("Unable to get hostname or IP Address.\n")
