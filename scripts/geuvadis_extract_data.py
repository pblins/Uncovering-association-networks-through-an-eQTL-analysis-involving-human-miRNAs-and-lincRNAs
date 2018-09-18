#!/usr/bin/python

import sys

######################## OUTLINE #########################
# THIS SCRIPT MAP GEUVADIS DATA TO SNPS RS ID AND  	 #
# GENERATE AN OUTPUT FILE WITH GENOTYPE INFO		 #
##########################################################

######################## PARAMS ##########################
# INPUT 1: RS ID MAP FILE 				 #
# INPUT 2: GEUVADIS VCF FILE 				 #
# OUTPUT: GENOTYPE BY SNP FILE 				 #
##########################################################

RS_ID_FILE = sys.argv[1]

snp_id_to_rs_id = dict()

f = open(RS_ID_FILE, "r")

for line in f:
	line = line.rstrip()
	s = line.split("\t")
	snp_id_to_rs_id[s[1]] = s[0]

f.close()

GEUVADIS_FILE = sys.argv[2]

f = open(GEUVADIS_FILE, "r")

for line in f:
	
	if line.startswith("##"):
		continue

	if line.startswith("#"):
		line = line.rstrip()
		s = line.split("\t")
		print s[2] + "\t",
		for i in range(9, len(s)):
			print s[i] + "\t",
		print ""
		continue

	line = line.rstrip()
	s = line.split("\t")
	print snp_id_to_rs_id[s[2]] + "\t",
	for i in range(9, len(s)):
		print s[i].split(":")[0] + "\t",
	print ""

f.close()
