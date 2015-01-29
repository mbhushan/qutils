import subprocess
import shlex
import sys


def testPing(host):
    command_line = "ping -c 1 " + host
    args = shlex.split(command_line)
    try:
        subprocess.check_call(args, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
        print "Server: %s is UP!" % host
    except subprocess.CalledProcessError:
        print "PING FAILED TO SERVER: %s" % host


def main():
    if len(sys.argv) < 2:
        print "Please provide domain url as command line arguments"
        print "Example: python host_ping.py www.google.com"
    else:
        host = sys.argv[1]
        testPing(host)


if __name__ == '__main__':
    main()
