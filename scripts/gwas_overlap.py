#!/usr/bin/python

import sys

snp_gwas = dict()

######################## OUTLINE #########################
# THIS SCRIPT OVELAPS THE SIGNIFICANT SNPS WITH 		 # 
# GWAS DATA												 #
##########################################################

######################## PARAMS ##########################
# INPUT 1: GWAS DATA FILE 								 #
# INPUT 2: SIGNIFICANT SNPS FILE						 #
# OUTPUT: OVERLAPPING RESULT FILE 						 #
##########################################################

GWAS_FILE = sys.argv[1]
SIGNIF_SNPS_FILE = sys.argv[2]

with open(GWAS_FILE, 'r') as f:
	for line in f:
		line = line.rstrip()
		s = line.split("\t")
		snp_gwas[s[7]] = line


with open(SIGNIF_SNPS_FILE, 'r') as f:
	for line in f:
		line = line.rstrip().split("\t")
		snp = line[1][1:-1]
		if snp in snp_gwas.keys():
			print line + "\t" + snp_gwas[line]
