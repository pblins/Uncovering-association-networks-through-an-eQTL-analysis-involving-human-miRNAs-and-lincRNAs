#!/usr/bin/python

import sys
from db_connection import connect
from genotype import get_snp_genotype

######################## OUTLINE #########################
# THIS SCRIPT MAPS GEUVADIS DATA TO SNP RS ID AND        #
# USES A MYSQL DATABASE CREATED OVER GEUVADIS DATA TO	  #
# GENERATE AN OUTPUT FILE WITH GENOTYPE INFO		  #
##########################################################

######################## PARAMS ##########################
# INPUT 1: SNP CATALOG FILE				  #
# INPUT 2: SAMPLE ID FILE				  #
# INPUT 3: OUTPUT PATH					  #
# OUTPUT: GENOTYPE GENE EXPRESSION BY SAMPLE		  #
##########################################################

DB = connect()
DB_CURSOR = DB.cursor()

HO_1 = "0" # 0/0
HE = "1" # 1/0 or 0/1
HO_2 = "2" # 1/1

CATALOG_FILE = sys.argv[1]
SAMPLE_FILE = sys.argv[2]
OUT_PATH = sys.argv[3]

snp_to_gene = dict()
snp_to_chr = dict()

file = open(CATALOG_FILE, 'r')

for line in file:
	s = line.rstrip().split("\t")
	snp_to_gene[s[3]] = s[6]
	snp_to_chr[s[3]] = s[0]
file.close()


samples = []

s_file = open(SAMPLE_FILE, 'r')
for sample in s_file:
	samples.append(sample)
s_file.close()

for snp in snp_to_gene.keys():

	CHR = snp_to_chr[snp]
	if CHR == "X" or CHR == "Y":
		continue

	FILE_GENOTYPE = "../../data/genotype/chr" + CHR + "_allelic_info.txt"
	FILE_EXPRESSION = "../data/expression/chr" + CHR + "_expression_data.txt"

	DB_CURSOR.execute("SELECT * FROM chr" + CHR + "_snps WHERE snp='" + snp + "\n';")
	snp_id = DB_CURSOR.fetchone()
	if snp_id <= 0:
		continue

	DB_CURSOR.execute("SELECT * FROM chr" + CHR + "_genes WHERE gene='" + snp_to_gene[snp] + "';")
	gene_id = DB_CURSOR.fetchone()
	if gene_id <= 0:
		continue

	genotypes = get_snp_genotype(FILE_GENOTYPE, snp_id[0]).rstrip().split("\t")
	genotype = ""
	alleles = []

	output = open(OUT_PATH + gene_id[1] + "_" + snp + "_expression.txt", "w")
	output.write("")
	output.close()
	output = open(OUT_PATH + gene_id[1] + "_" + snp + "_expression.txt", "a")
	for i in range(0,len(genotypes)):
		DB_CURSOR.execute("SELECT * FROM samples WHERE sample='" + samples[i] + "';")
		sample_id = DB_CURSOR.fetchone()
		if sample_id <= 0:
			continue

		DB_CURSOR.execute("SELECT * FROM chr" + CHR + "_expression WHERE geneid=" + str(gene_id[0]) + " AND sampleid=" + str(sample_id[0]) + ";")
		expression = DB_CURSOR.fetchone()
		if expression <= 0:
			continue

		if len(genotypes[i].split("/")) > 1:
			alleles = genotypes[i].split("/")
		else:
			alleles = genotypes[i].split("|")

		if alleles[0] == "0" and alleles[1] == "0":
			genotype = HO_1
		elif alleles[0] == "1" and alleles[1] == "1":
			genotype = HO_2
		else:
			genotype = HE

		output.write(sample_id[1] + "\t" + genotype + "\t" + str(expression[3]) + "\n")

	output.close()
