import socket
import struct
from time import ctime

NTP_SERVER = "0.uk.pool.ntp.org"
TIME1970 = 2208988800L


def sntp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = '\x1b' + 47 * '\0'
    client.sendto(data, (NTP_SERVER, 123))
    data, address = client.recvfrom(1024)
    if data:
        print "Response recieved from: ", address
    t = struct.unpack('!12I', data)[10]
    t -= TIME1970
    print "\tTIME = %s" % (ctime(t))


def main():
    sntp_client()


if __name__ == '__main__':
    main()