import threading
import os
from ForkingServer import ForkingServer
from ForkedClient import ForkedClient
from ForkingServerRequestHandler import ForkingServerRequestHandler


SERVER_HOST = 'localhost'
SERVER_PORT = 0     # tells the kernel to pick up a port dynamically
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server!'


def main():
    # launch the server
    server = ForkingServer((SERVER_HOST, SERVER_PORT),
                           ForkingServerRequestHandler)
    ip, port = server.server_address

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)   # Dont hang on exit
    server_thread.start()
    print "Server loop running PID: %s" % os.getpid()

    # Launch the clients
    client1 = ForkedClient(ip, port)
    client1.run()

    client2 = ForkedClient(ip, port)
    client2.run()

    # lets clean them up
    server.shutdown()
    client1.shutdown()
    client2.shutdown()
    server.socket.close()


if __name__ == '__main__':
    main()
