#!/usr/bin/python

import os
import sys
from scipy.stats import spearmanr
from statsmodels.sandbox.stats.multicomp import multipletests

######################## OUTLINE #########################
# THIS SCRIPT PERFORMS AN eQTL ANALYSIS BASED IN THE     # 
# SPEARMAN CORRELATION TEST AND BENJAMIN-HOCHBERG        #
# MULTIPLE TEST CORRECTION                               #
##########################################################

######################## PARAMS ##########################
# INPUT 1: GENOTYPE GENE EXPRESSION BY SAMPLE PATH       #
# (INPUT FILE -TAB DELIMITED- WITH THE FOLLOWING         # 
# COLUMNS: A - SAMPLE, B - NUMERIC RECORD GENOTYPES FOR. #
# ADDITIVE MODEL -Ex.: AA - 0, AB - 1, BB - 2).          #
# OUTPUT: eQTL FILE WITH "SNP", "GENE", "P-VALUE",       # 
# "CORRECTED P-VALUE", AND "SPEARMAN CORRELATION"        #
##########################################################

def eqtl(path):

        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

        pvals = []
        snps = []
        rhos = []
        genes = []

        for f in files:

                samples = []
                genotypes = []
                rpkm = []

                with open(path + f, "r") as filestream:
                        for line in filestream:
                                try:
                                        sample, genotype, exp = line.rstrip().split("\t")
                                except:
                                        continue

                                samples.append(sample)
                                genotypes.append(genotype)
                                rpkm.append(float(exp))

                rho, pval = spearmanr(genotypes, rpkm)
        	
                pvals.append(pval)
                rhos.append(rho)
        	snps.append(f.split("_")[1])
                genes.append(f.split("_")[0])


        header = "\t".join(["snp", "gene", "pval", "corrected_pval", "correlation"])

        corr_pvals = multipletests(pvals, alpha=0.5, method='fdr_bh', returnsorted=False)

        with open(path + "eqtl.dat", "w") as out:
                out.write(header + "\n")
                for i in range(0,len(snps)):
                        out.write("\t".join([snps[i], genes[i], str(pvals[i]), str(corr_pvals[1][i]), str(rhos[i])]) + "\n")
        
if __name__ == '__main__':

        try:
                eqtl(sys.argv[1])

        except Exception as e:
                print str(e)
                sys.exit(2)