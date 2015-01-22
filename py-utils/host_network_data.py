# python2.7


import socket


def convertData(data):
    print "Original data: ", data
    print "Long Host byte order: ", socket.ntohl(data)
    print "Long Network byte order: ", socket.htonl(data)

    try:
        print "Short Host byte order: ", socket.ntohs(data)
        print "Short Network byte order: ", socket.htons(data)
    except:
        print "integer overflow!"


def readInputData():
    while True:
        data = raw_input("Enter data: ")
        try:
            data = int(data)
            return data
        except:
            print "Bad data - please input integer data"


def main():
    data = readInputData()
    convertData(data)


if __name__ == '__main__':
    main()
