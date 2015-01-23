import socket
import os


SERVER_HOST = 'localhost'
SERVER_PORT = 0     # tells the kernel to pick up the port dynamically
BUF_SIZE = 1024
ECHO_MSG = "Hello Echo Server"


class ForkedClient:
    """ A client to test forking server """
    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))

    def run(self):
        """ Client playing with the server"""
        # send data to client
        currProcessID = os.getpid()
        print "PID: %s sending echo message to server: %s" % (currProcessID,
                                                              ECHO_MSG)
        sentDataLen = self.sock.send(ECHO_MSG)
        print "Sent: %d characters so far..." % sentDataLen

        # Display server response
        response = self.sock.recv(BUF_SIZE)
        print "PID %s recieved: %s" % (currProcessID, response[5:])

    def shutdown(self):
        """ cleaning up the socket connection """
        self.sock.close()
