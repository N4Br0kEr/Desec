#!/usr/bin/python

import socket,sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if s.connect_ex(("whois.iana.org",43)) == 0:
	s.send(sys.argv[1]+"\r\n")
else:
	print "Error"

resp = s.recv(1024).split()
print "[*] O whois e %s " % (resp[19])
whois = resp[19]
so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
so.connect((whois,43))
so.send(sys.argv[1]+"\r\n")

r =  so.recv(1024)
print r 

