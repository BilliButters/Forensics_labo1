import exiftool
import os
import sys
from collections import Counter

dossier = os.listdir("/home/nico/Forensics/labo1/partie2/documents_heaj/")


liste_vide = []

def metadata(dossier, liste_vide):
	with exiftool.ExifTool() as et:
		metadata = et.get_metadata_batch(dossier)
	for d in metadata:
		for k,v in d.items():
			if k not in liste_vide:
				liste_vide.append(k)

metadata(dossier, liste_vide)

liste_vide.sort()
print(liste_vide, "\n\n")

argument_metadata = sys.argv[1]


def meta_print(liste_vide, argument_metadata, dossier):
	i = 0
	liste_info = []
	with exiftool.ExifTool() as et:
                metadata = et.get_metadata_batch(dossier)
	for d in metadata:
		for k,v in d.items():
			if k == argument_metadata:
				liste_info.append(v)
	compteur_occurrence = Counter(liste_info).most_common()
	print(compteur_occurrence)

meta_print(liste_vide, argument_metadata, dossier)
