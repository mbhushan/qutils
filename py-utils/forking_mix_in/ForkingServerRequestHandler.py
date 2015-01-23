import SocketServer
import os


BUF_SIZE = 1024


class ForkingServerRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        # send the echo back to the client
        data = self.request.recv(BUF_SIZE)
        curr_pid = os.getpid()
        response = "%s : %s" % (curr_pid, data)
        print "Server requesting response: %s" % response
        self.request.send(response)
        return
