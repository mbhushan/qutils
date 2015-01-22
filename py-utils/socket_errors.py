import socket
import argparse
import sys


def testSocketErrors():
    # setup argument parsing
    parser = argparse.ArgumentParser(description="Socket Error Example")
    parser.add_argument('--host', action="store", dest="host", required=False)
    parser.add_argument('--port', action="store", dest="port", type=int,
                        required=False)
    parser.add_argument('--file', action="store", dest="file", required=False)

    givenArgs = parser.parse_args()
    host = givenArgs.host
    port = givenArgs.port
    filename = givenArgs.file

    # first try-except block - create socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print "Error creating socket: %s" % e
        sys.exit(1)

    # second try- except block - connect to host and port
    try:
        sock.connect((host, port))
    except socket.gaierror, e:
        print "Address related error connecting to server: %s" % e
        sys.exit(1)
    except socket.error, e:
        print "Connection error: %s" % e
        sys.exit(1)

    # third try-except block - sending data
    try:
        sock.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
    except socket.error, e:
        print "Error sending data: %s" % e
        sys.exit(1)

    while True:
        # Fourth try-catch block -- waiting to recieve data from remote host
        try:
            buf = sock.recv(2048)
        except socket.error, e:
            print "Error recieving data: %s" % e
            sys.exit(1)
        if not len(buf):
            break
        # write the recieved data
        sys.stdout.write(buf)


def main():
    testSocketErrors()


if __name__ == '__main__':
    main()
