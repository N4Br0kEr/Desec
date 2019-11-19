#!/usr/share/python

import sys
def dns():
	import socket
	dns = raw_input("Site: ")
	resp = socket.gethostbyname(dns)
	print "IP ====> %s" % (resp) 	
def ajuda():
	print "Modo de Uso: "
	print " python funcao.py dns"
	print ""
	print " python funcao.py whois"
	print ""
	print " python fucao.py scan"
	print ""
def scan():
	import socket
	alvo = raw_input("Alvo: ")
	port = input("Port: ")
	so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if so.connect_ex((alvo,port)) == 0:
		banner = so.recv(1024)
		print "PORTA %s [ABERTA]" % (port)
		print "Banner : "
		print banner
	else:
		print "PORTA %s [FECHADA]" % (port)
def whois():
	import socket
	site = raw_input("Site: ")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if s.connect_ex(("whois.iana.org",43)) == 0:
		s.send(site+"\r\n")
	else:
		print "Ocorreu um erro"
		print ":("
	resp = s.recv(1024).split()
	# print "[*] Whois usado foi o %s " %s (resp[19])
	whois = resp[19]
	so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	so.connect((whois,43))
	so.send(site+"\r\n")
	resp2 = so.recv(1024)
	print resp2
	#close(so)
	#close(s)


if len(sys.argv) <= 1:
	ajuda()
elif sys.argv[1] == "dns":
	dns()
elif sys.argv[1] == "whois":
	whois()
elif sys.argv[1] == "scan":
	scan()



	



