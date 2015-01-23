import socket
import argparse

HOST = 'localhost'


def echoClient(port):
    """ A simple echo client """
    # create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverAddr = (HOST, port)
    print "Connecting to %s port %s" % serverAddr
    sock.connect(serverAddr)

    # send data
    try:
        message = "please echo this very important message"
        print "sending .. %s" % message
        sock.sendall(message)

        # look for response
        amt_recieved = 0
        amt_expected = len(message)
        while amt_recieved < amt_expected:
            data = sock.recv(16)
            amt_recieved += len(data)
            print "Recieved: %s" % data
    except socket.errno, e:
        print "Socket error: %s" % str(e)
    except Exception, e:
        print "Other exception: %s" % str(e)
    finally:
        print "Closing connection to the server"
        sock.close()


def main():
    parser = argparse.ArgumentParser(description="Socket Server Example")
    parser.add_argument('--port', action='store', type=int, required=True)
    givenArgs = parser.parse_args()
    port = givenArgs.port
    echoClient(port)


if __name__ == '__main__':
    main()
