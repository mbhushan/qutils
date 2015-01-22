# python 2.7

import socket
# import sys


def reuse_sock_addr():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "OLD socket state: ", old_state

    # let enable SO_REUSEADDR option
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "NEW socket state: ", new_state
    local_port = 8282

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(('', local_port))
    srv.listen(1)
    print "Listening on port: %s" % local_port

    while True:
        try:
            conn, addr = srv.accept()
            print "Connected by %s: %s" % (addr[0], addr[1])
        except KeyboardInterrupt:
            break
        except socket.error, msg:
            print "%s" % (msg)


def main():
    reuse_sock_addr()


if __name__ == '__main__':
    main()
