# -*- coding: latin-1 -*-
import os.path
import threading
import socket
import sqlite3
import platform


def kh_simple(kh_path):
	global kh_ecriture
	if not kh_path[-1] == "/":
		kh_path = kh_path + "/"
	kh_nb = kh_path.count("/")
	kh_ecriture = "debianeuf\n"
	for root, dirs, fichier in os.walk(kh_path):  
		for i in fichier:
			kh_var = (os.path.join(root, i)) + "}]{" + str(os.path.getmtime(os.path.join(root, i)))
			trouver = lambda mot, lettre: [i for i, car in enumerate(mot) if car==lettre]
			kh_trouver = trouver(kh_var, "/")
			if platform.system() == "Windows":
				kh_var = kh_var.replace("\\", "/")
				print("changé")
			kh_ecriture = kh_ecriture + kh_var[kh_trouver[kh_nb-1]:] + "\n"
	print(kh_ecriture)

kh_simple("C:/Users/antoine/Documents/Bandicam/Nouveau dossier")

class ClientThread(threading.Thread):
    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self):
   
        print("Connection de %s %s" % (self.ip, self.port, ))

        threading.Thread(target=kh_simple, args="C:/Users/antoine/Documents/Bandicam/Nouveau dossier").start

        r = self.clientsocket.recv(2048)
        st = str(r)
        print(st)
        print(kh_ecriture)
        self.clientsocket.sendall(kh_ecriture.encode())


        print("Client déconnecté... et ")

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",1111))


while True:
    tcpsock.listen(10)
    print( "En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()



