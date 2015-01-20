import socket


def getMachineInfo():
    remoteHost = raw_input("Enter remote hostname: ")
    try:
        print "IP address of %s" % socket.gethostbyname(remoteHost)
    except socket.error, err_msg:
        print "%s: %s" % (remoteHost, err_msg)


def main():
    getMachineInfo()

if __name__ == '__main__':
    main()
