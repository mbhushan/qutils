import ntplib
from time import ctime


def getInternetTime():
    ntpClient = ntplib.NTPClient()
    response = ntpClient.request('pool.ntp.org')
    print "Time on Internet Time Server: ", ctime(response.tx_time)


def main():
    getInternetTime()


if __name__ == '__main__':
    main()
