#!/usr/bin/python

import sys
from os import listdir
from os.path import isfile, join

######################## OUTLINE #########################
# THIS SCRIPT OVELAPS THE SNP CATALOG WITH GTEX DATA 	  #
##########################################################

######################## PARAMS ##########################
# INPUT 1: CATALOG FILE					 #
# INPUT 2: GTEX eQTL DATA PATH				  #
# INPUT 3: OUTPUT PATH					  #
# OUTPUT: ONE FILE PER TISSUE WITH THE RESULT OF	  #
# OVERLAPPING						  #
##########################################################

snps = dict()

CATALOG_FILE = sys.argv[1]
GTEX_FILES_PATH = sys.argv[2]
OUT_PATH = sys.argv[3]

with open(CATALOG_FILE, 'r') as f:
	for line in f:
		s = line.rstrip().split("\t")
		id = "_".join([s[0], s[1], s[4], s[5], "b37"])
		snps[id] = line.rstrip()


gtex_files = [f for f in listdir(GTEX_FILES_PATH) if isfile(join(GTEX_FILES_PATH, f))]
for f in gtex_files:
	tissue = f.split(".V6p.")[0]

	with open(path + f, 'r') as stream:
		header = stream.readline()
		out = open(OUT_PATH + tissue + ".txt", 'a')
		for line in stream:
			s = line.rstrip().split("\t")[0]
			try:
				out.write(snps[s] + "\t" + line)
			except:
				continue
		out.close()
