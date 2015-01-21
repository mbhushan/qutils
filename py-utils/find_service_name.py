# python-2.7  -> may work with other versions
# manib

import socket


def findServiceName(ports):
    print "%6s:%15s" % ("port", "service")
    for p in ports:
        try:
            service = socket.getservbyport(p)
            print "%6d:%16s" % (p, service)
        except:
            continue


def readPort():
    while True:
        port = raw_input()
        if not port.isdigit():
            print "Invalid Port. Try again.."
            continue
        port = int(port)
        if port < 1 or port > 65535:
            print "Invalid Port. Port ranges are 1 to 65535"
            print "Try Again.."
            continue
        return port


def readPortRange():
    print "Enter start port: "
    start_port = readPort()
    print "Enter end port: "
    end_port = readPort()
    if start_port > end_port:
        start_port, end_port = end_port, start_port

    ports = []
    for i in range(start_port, end_port):
        ports.append(i)

    return ports


def main():
    ports = readPortRange()
    findServiceName(ports)


if __name__ == '__main__':
    main()
