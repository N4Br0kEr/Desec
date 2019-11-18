#!/usr/share/python

import socket

alvo = raw_input("Digite o IP : ")
port = input("Digite a Porta : ")
so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if so.connect_ex((alvo,port)) == 0:
	banner = so.recv(1024)
	print "Porta %s [ABERTA]" % (port)
	print "Banner :" 
	print banner
else:
	print "Porta %s [FECHADA] " % (port)
	
