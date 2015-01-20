import socket
import sys


def getMachineInfo():
    host_name = raw_input("Enter host name: ")
    host_name = host_name.strip()
    # host_name = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(host_name)
    except:
        print "BAD Hostname!"
        sys.exit()
    print "Host name: %s" % host_name
    print "IP address: %s" % ip_address


def main():
    getMachineInfo()


if __name__ == '__main__':
    main()
