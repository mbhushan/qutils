import socket
import threading
import SocketServer

SERVER_HOST = 'localhost'
SERVER_PORT = 0     # tells kernel to pick up a port dynamically
BUF_SIZE = 1024


def client(ip, port, message):
    """ A client to test threading mix in server """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(BUF_SIZE)
        print "client recieved: %s" % response
    finally:
        sock.close()


class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    """ an example of threaded TCP request handler """
    def handle(self):
        data = self.request.recv(BUF_SIZE)
        curr_thread = threading.current_thread()
        response = "%s : %s" % (curr_thread.name, data)
        self.request.sendall(response)


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """ nothing to add here - inherited everything from parent """
    pass


def main():
    server = ThreadedTCPServer((SERVER_HOST, SERVER_PORT),
                               ThreadedTCPRequestHandler)
    ip, port = server.server_address
    # start a thread with the server - one thread per request
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running on thread: %s" % server_thread.name

    # run client
    client(ip, port, "Hello from client-1")
    client(ip, port, "Hello from client-2")
    client(ip, port, "Hello from client-3")

    server.shutdown()

if __name__ == '__main__':
    main()
