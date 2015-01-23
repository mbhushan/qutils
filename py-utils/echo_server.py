import socket
import argparse


HOST = 'localhost'
BACKLOG = 5
DATA_PAYLOAD = 2048


def echoServer(port):
    """ A simple echo server """
    # create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind the socket to the port
    serverAddr = (HOST, port)
    print "Starting echo server on %s: port:%s" % serverAddr
    sock.bind(serverAddr)

    # Listen to clients, backlog specifies max no. of queued connections
    sock.listen(BACKLOG)

    while True:
        print "Waiting to recieve message from client"
        client, address = sock.accept()
        data = client.recv(DATA_PAYLOAD)
        if data:
            print "DATA: %s" % data
            client.send(data)
            print "sent %s bytes back to %s" % (data, address)
        client.close()


def main():
    parser = argparse.ArgumentParser(description="Socket Server Example")
    parser.add_argument("--port", action="store", dest="port", type=int,
                        required=True)
    giveArgs = parser.parse_args()
    port = giveArgs.port
    echoServer(port)


if __name__ == '__main__':
    main()
