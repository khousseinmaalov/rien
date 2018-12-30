# -*- coding: latin-1 -*-
import socket
from os.path import exists
from os import mkdir
import os
import urllib.request


sdestr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sdestr.connect(("127.0.0.1", 1111))
print("envoie de données: ")
value = "rien"
sdestr.send(value.encode())
r = sdestr.recv(9999999)
r = r.decode()

with open("kh_fichier.txt", "r") as kh_ma:
	kh_read = kh_ma.read()

trouver = lambda mot, lettre: [i for i, car in enumerate(mot) if car==lettre]

kh_trouver_tele = trouver(kh_read, "\n")

def on_enleve_ce_qui_est_inutile():
	global kh_read
	debianeuf = 0
	kh_count = kh_read.count("\n")


	while debianeuf < kh_count-1:
		amd = kh_read[kh_trouver_tele[debianeuf]:kh_trouver_tele[debianeuf+1]]
		nvidia = amd.find("}]{")
		intel = amd[:nvidia]
		if not intel in r:
			kh_read = kh_read.replace(amd, "")
		debianeuf = debianeuf + 1

	print(kh_read)

on_enleve_ce_qui_est_inutile()

kh_count = r.count("\n")


kh_trouver_tele = trouver(r, "\n")


debianeuf = 0

while debianeuf < kh_count-1:
	amd = r[kh_trouver_tele[debianeuf]:kh_trouver_tele[debianeuf+1]]
	nvidia = amd.find("}]{")
	intel = amd[:nvidia]
	electrum = intel.count("/")
	if electrum > 1:
		kh_trouver= trouver(intel, "/")
		kh_mkdir = intel[2:kh_trouver[-1]]
		if exists(kh_mkdir) == False:
			mkdir(kh_mkdir)
	if not intel in kh_read:
		kh_read = kh_read + amd
		print("https://github.com/debianeuf/download/blob/master/" + intel[2:] + "?raw=true", intel[2:])
		try:
			urllib.request.urlretrieve("https://github.com/debianeuf/download/blob/master/" + intel[2:] + "?raw=true", intel[2:])
		except urllib.error.HTTPError:
			print("erreur: impossible de telecharger le fichier: ")
		except urllib.error.URLError:
			print("erreur lors du telechargement: svp veuillez verifier votre connexion")
	else:
		if not amd in kh_read:
			ether = kh_read.find(intel[1:])
			litecoin = kh_read.find("\n", ether)

			print("https://github.com/debianeuf/download/blob/master/" + intel[2:] + "?raw=true", intel[2:])
			try:
				urllib.request.urlretrieve("https://github.com/debianeuf/download/blob/master/" + intel[2:] + "?raw=true", intel[2:])
			except urllib.error.HTTPError:
				print("erreur: impossible de telecharger le fichier: ")
			except urllib.error.URLError:
				print("erreur lors du telechargement: svp veuillez verifier votre connexion")
				kh_read = kh_read.replace(kh_read[ether:litecoin], amd[1:])

		else:
			print("on passe")


	debianeuf  = debianeuf + 1

with open("kh_fichier.txt", 'w') as everything:
	everything.write(kh_read)