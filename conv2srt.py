#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import re
import sys

if len(sys.argv) == 2 :
	f = open(sys.argv[1])
else :
	f = sys.stdin

# Motifs de recherche
patEntete = re.compile("^WEBVTT$")
patTime = re.compile("^[0-9][0-9]:[0-9][0-9]:")
patCoulDeb = re.compile(r"<c\.(\w+)>", re.IGNORECASE)
patCoulFin = re.compile(r"</c>")

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

	# lignes correspondant à un code couleur : début
	ligne = patCoulDeb.sub(r'<font color="\1">', ligne)

	# lignes correspondant à un code couleur : fin
	ligne = patCoulFin.sub("</font>", ligne)

	# les autres lignes sans changement
	print ligne

