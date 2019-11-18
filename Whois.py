#!/usr/share/python

import socket
site = raw_input("Site :")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if s.connect_ex(("whois.iana.org",43)) == 0:
	s.send(site+"\r\n")
else:
	print "Ocorreu um erro "
	print ":("
resp = s.recv(1024).split()
print "[*] O whois e %s " % (resp[19])
whois = resp[19]
so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so.connect((whois,43))
so.send(site+"\r\n")
resp2 = so.recv(1024)
print resp2
close(so)
close(s)
 
