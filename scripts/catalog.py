#!/usr/bin/python

from os import system
import sys

######################## OUTLINE #########################
# THIS SCRIPT USES BEDTOOLS SOFTWARE TO PERFORM THE      #
# DBSNP CATALOG                                          #
##########################################################

######################## PARAMS ##########################
# INPUT 1: BED FILE OF DBSNP DATA						 #
# INPUT 2: BED FILE OF REGULATORY REGION TO INTERSECT    #
# INPUT 3: NAME OF OUTPUT FILE 						     #
# OUTPUT : CATALOG FILE                                  #
##########################################################

DBSNP_FILE = sys.argv[1]
INTERSECT_REGION_FILE = sys.argv[2]
OUT_FILE = sys.argv[3]

system("bedtools intersect -a " + DBSNP_FILE + " -b " + INTERSECT_REGION_FILE + " -wa -wb >" + OUT_FILE)