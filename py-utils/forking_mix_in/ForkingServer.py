import SocketServer


class ForkingServer(SocketServer.ForkingMixIn,
                    SocketServer.TCPServer):
    """ Nothing to add here - inherited everything from parents """
    pass
