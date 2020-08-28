
from socket import *

socket = socket(AF_INET, SOCK_STREAM)

def retbanner(ip,port):
    try:
        setdefaulttimeout(2)
        socket.connect((ip,port))
        banner = socket.recv(1024)
        return banner
    except:
        return    

def main():
    ip = raw_input("Enter the IP :")
    for port in range (1,100):
        banner = retbanner(ip,port)
        if banner:
            print ("[+]" + ip + "/" + str(port) + " : " + banner)

if __name__ == '__main__':
    main()          



# o/p: Enter the IP :192.168.31.162
# [+]192.168.31.162/25 : 220 caavo-Inspiron-3542 ESMTP Postfix (Ubuntu)