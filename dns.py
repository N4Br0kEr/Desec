#!/usr/share/python

import socket

dns = raw_input("Site : ")

resp = socket.gethostbyname(dns)

print "IP ===> %s" % (resp)


