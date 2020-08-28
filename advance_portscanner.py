from socket import *
from optparse import *
from threading import *
from termcolor import colored, cprint

def connScan(tgtHost,tgtPort):
    sock = socket(AF_INET, SOCK_STREAM)
    if sock.connect_ex((tgtHost,tgtPort)):
        print (colored("[!!] port %d is closed "% (tgtPort), "red"))
    else:
        cprint ("[*] port %d is opened"% (tgtPort), "yellow", "on_magenta", attrs=["bold","blink"])

def portScan(tgtHost,tgtPorts):
    print (tgtHost, tgtPorts)
    try:
        tgtIP = gethostbyname(tgtHost)
    except:    
        print ("Unknown host %s " %tgtHost)
    try:
        tgtName = gethostbyaddr(tgtIP)
        print ("[+] scan result for : " + tgtName[0])
    except:    
        print ("[+] scan result for : " + tgtIP)    
    setdefaulttimeout(2)
    for tgtPort in tgtPorts:
        t = Thread(target = connScan, args=(tgtHost,int(tgtPort)))
        t.start()
    
def main():
    parser = OptionParser('Usage of Program: ' + '-H <target Host> -p <target Port>')
    parser.add_option('-H', dest = 'tgtHost', type = 'string', help = 'specify target host ')
    parser.add_option('-p', dest = 'tgtPort', type = 'string', help = 'specify target port ')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(",")
    
    if (tgtHost == '0') | (tgtPorts[0] == '0'):
        print (parser.usage)
        exit(0)
    portScan(tgtHost,tgtPorts)    

if __name__ == '__main__':
    main()
