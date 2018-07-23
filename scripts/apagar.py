#!/usr/bin/python

import os

path = "/Users/paulobranco/Documents/Bioinformatica/snpdb_mapping/git_repository/example/genotype_expression_folder/"

files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
conversor = {'ho1' : 0, 'he' : 1, 'ho2' : 2}

for f in files:
	out = open(path + "c_" + f, "w")
	with open(path + f, "r") as stream:
		for line in stream:
			try:
				sample, genotype, expression = line.rstrip().split("\t")
				out.write("\t".join([sample, str(conversor[genotype]), expression]) + "\n")
			except:
				continue
	out.close()