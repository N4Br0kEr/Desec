#!/usr/share/python

import sys
def TcpServer():
	import socket
	port = input("[*] Porta : ")
	server_address = ('localhost', port)
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(server_address)
	server.listen(5)
	print "[*] Escutando no %s na porta %s " % (server_address)
	while True:
		print "[*] Esperando conexoes" 
		connection, client_address = server.accept()
		try:
			print "[*] Conectado no", client_address
			while True:
				data = connection.recv(1024)
				print "[*] Recebido %s " % (data)
			if data:
				print "[*] Enviando Dados"
				connection.sendall(data)
			else :
				print "[*] Nao tem mais dados do",client_address
				break
		finally:
			connection.close()
def dnsr():
	import socket
	
	dns = raw_input("IP : ")
	dns_reverse = socket.gethostbyaddr(dns)
	print dns_reverse[0]
def dns():
	import socket
	dns = raw_input("Site: ")
	resp = socket.gethostbyname(dns)
	print "IP ====> %s" % (resp) 	
def ajuda():
	print "Modo de Uso: "
	print " python test02.py dns"
	print ""
	print " python test02.py whois"
	print ""
	print " python test02.py scan"
	print ""
	print "python test02.py dnsrecv "
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
elif sys.argv[1] == "dnsr":
	dnsr()
elif sys.argv[1] == "tcp":
	TcpServer()


	



