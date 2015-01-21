# python-2.7 - may run with other versions with/without modifications
# manib


import socket
import sys
from binascii import hexlify


def convertIP4Address():
    ip_addr = readIPAddress()
    try:
        packed_ip_addr = socket.inet_aton(ip_addr)
    except:
        print "Invalid IP Address!"
        sys.exit()
    unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)

    print "IP Address: %s => Packed: %s, Unpacked: %s"\
        % (ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr)


def readIPAddress():
    print "Enter IP Address: "
    ip_addr = raw_input()
    return ip_addr.strip()


def main():
    convertIP4Address()


if __name__ == '__main__':
    main()
