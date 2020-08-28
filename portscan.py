import socket
from termcolor import colored, cprint
# socket.AF_INET => for IPV4/IPV6 address package
# socket.SOCK_STREAM => for TCP package 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"

def portscanner(port):
    if sock.connect_ex((host,port)):
        print (colored("[!!] port %d is closed "% (port), "red"))
    else:
        cprint ("[*] port %d is opened"% (port), "yellow", "on_magenta", attrs=["bold","blink"])

for port in range (1,1000):
    portscanner(port)