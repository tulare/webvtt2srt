#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import re
import sys

if len(sys.argv) == 2 :
	f = open(sys.argv[1])
else :
	f = sys.stdin

patEntete = re.compile("^WEBVTT$")
patTime = re.compile("^[0-9][0-9]:[0-9][0-9]:")

numline = -1
numblock = 0

# Parcourir les lignes du fichier
for line in f :
	ligne = line.strip()
	numline += 1

	# Vérifier l'entête WEBVTT et l'enlever
	if numline == 0 :
		if patEntete.search(ligne) :
			continue
		else :
			print >> sys.stderr, "Erreur format fichier entrée"
			sys.exit(1)

	# Enlever également la ligne vide derrière l'entête
	if numline == 1 :
		continue

	# lignes correspondant à un motif temporel
	# placer un numéro avant le bloc
	# remplacer "." par ","
	if patTime.search(ligne) :
		numblock += 1
		print numblock
		print ligne.replace(".", ",")
		continue

	# les autres lignes sans changement
	else :
		print ligne

