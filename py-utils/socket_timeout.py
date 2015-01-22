# python-2.7
import socket


def readTimeOutValue():
    while True:
        timeout = raw_input("Enter timeout(in seconds) value: ")
        try:
            timeout = int(timeout)
            return timeout
        except:
            print "Bad value - please try again.."


def setSocketTimeOut(timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Default timeout value: ", sock.gettimeout()

    sock.settimeout(timeout)
    print "Current socket timout value: ", sock.gettimeout()


def main():
    timeout = readTimeOutValue()
    setSocketTimeOut(timeout)


if __name__ == '__main__':
    main()
