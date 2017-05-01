#!/usr/bin/python
# -*- coding: utf-8 -*-

import fotogramas
import imdb
import filmaffinity

'''peliculas = ["Johnny English", "Di que sí", "Deep blue sea", "Juego de patriotas", "enemigos públicos", "rocky iv",
			 "el coloso en llamas", "casablanca", "la vida es bella", "el robobo de la jojoya", "lincoln", "cateto a babor",
			 "los minions", "cobra", "el olivo"]'''

peliculas = ["cobra"]


for p in peliculas:
	l1 = filmaffinity.buscar(p)
	l2 = fotogramas.buscar(p)
	l3 = imdb.buscar(p)

	print "FILMAFFINITY"
	for l in l1:
		print "\t" + l[0], l[1]

	print "FOTOGRAMAS"
	for l in l2:
		print "\t" + l[0], l[1]

	print "IMDB"
	for l in l3:
		print "\t" + l[0], l[1]

	print "====================================="
