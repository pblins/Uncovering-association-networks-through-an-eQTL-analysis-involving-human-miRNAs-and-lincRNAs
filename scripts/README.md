To generate the SNP catalog (step 1 of paper workflow), please follow the following instructions:
* CG-1. Get input data from public databases (check versions) used in the paper and convert to BED files.
* CG-2. Run catalog.py using dbSNP and Regulatory Region (miRNA, miRNA targets, lincRNA) BED files as input.

To generate the gEUVADIS analysis (step 2 of paper workflow), please follow the following instructions:

GE-1. Run geuvadis_extract_data.py using the vcf file (genotype) and rs id map file (both obtained from gEUVADIS portal) as input.

GE-2. Create an SQL database using gEUVADIS gene expression data. (cols: sampleid, gene_id, gene_exp)

GE-3. Run geuvadis_genotype_expression_by_sample.py using GE-1 and CG-2 outputs as input. Also name the path were the output files will be saved.

GE-4. Run geuvadis_eqtl.py using the directory path of GE-3 output files as input.

To generate the gEUVADIS analysis (step 2 of paper workflow), please follow the following instructions:

The output of GE-1 above will containg the data regarding WHATEVER1.
