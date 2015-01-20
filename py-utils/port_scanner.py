import socket
# import subprocess
import sys
from datetime import datetime


PORTS = 65535
# PORTS = 80


def scanPorts():
    # clean the slate
    # subprocess.call('clear', shell=True)

    # lets get the server details
    rserver = raw_input("Enter remote host to scan: ")
    rserver = rserver.strip()
    try:
        rserverIP = socket.gethostbyname(rserver)
    except:
        print "BAD Hostname!"
        sys.exit()

    # lets do some focasy before we scan
    print "-" * 60
    print "Please wait, scanning remote host: ", rserverIP
    print "-" * 60

    start = datetime.now()
    try:
        for port in range(1, PORTS):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0)
            # sadd = ('54.175.121.241', int(port))
            sadd = (rserverIP, port)
            result = sock.connect_ex(sadd)
            sock.settimeout(None)
            if result == 0:
                print "Port {}: \tOpen".format(port)
            # else:
            #    print "Port {}: \tClosed".format(port)
            sock.close()
    except KeyboardInterrupt:
        print "You pressed ctrl-C"
        sys.exit()
    except socket.gaierror:
        print "Host name could not be resolved - Exiting"
        sys.exit()
    except socket.error:
        print "Could not connect to Server."
        sys.exit()
    except:
        print "Some random error!"

    end = datetime.now()
    total = end - start
    print "Scan completed in: {} seconds".format(total)


def main():
    scanPorts()

if __name__ == '__main__':
    main()
