#!/usr/bin/python

import sys
from os import listdir
from os.path import isfile, join

######################## OUTLINE #########################
# THIS SCRIPT OVELAPS THE SIGNIFICANT SNPS WITH          # 
# PHARMGKB DATA                                          #
##########################################################

######################## PARAMS ##########################
# INPUT 1: PHARMGKB DATA FILE				  #
# INPUT 2: SIGNIFICANT SNPS FILE			  #
# OUTPUT: OVERLAPPING RESULT FILE			  #
##########################################################

PHARGKB_FILE = sys.argv[1]
SIGNF_SNPS_FILE = sys.argv[2]

genes = set()

with open(PHARGKB_FILE, 'r') as f:
	for line in f:
		line = line.rstrip()
		genes.add(line)

with open(SIGNF_SNPS_FILE, 'r') as f:
	for line in f:
		s = line.rstrip().split('\t')
		if s[0] in genes:
			print line.rstrip()
