import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096


def modifyBufSize():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get the size of the socket's send buffer
    bufSize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print "Buffer size [BEFORE]: %d", bufSize
    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)

    bufSize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print "Buffer size [AFTER]: %d", bufSize


def main():
    modifyBufSize()

if __name__ == '__main__':
    main()
