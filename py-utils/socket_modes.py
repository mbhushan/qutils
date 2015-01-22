# python 2.7
import socket


def testSocketModes():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(1)
    sock.settimeout(0.5)
    sock.bind(("127.0.0.1", 0))

    sock_addr = sock.getsockname()
    print "Trivial server launched on socket: %s" % str(sock_addr)

    while (1):
        sock.listen(1)


def main():
    testSocketModes()

if __name__ == '__main__':
    main()
