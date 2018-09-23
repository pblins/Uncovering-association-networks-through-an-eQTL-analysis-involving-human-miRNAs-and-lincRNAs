## Uncovering association networks through an eQTL analysis involving human miRNAs and lincRNAs

__To generate the SNP catalog (step 1 of paper workflow), please follow the instructions below:__
* CG-1. Get input data from public databases (check versions) used in the paper and convert to BED files.
* CG-2. Run `catalog.py` using dbSNP and Regulatory Region (miRNA, miRNA targets, lincRNA) BED files as input.

__To generate the gEUVADIS analysis (step 2 of paper workflow), please follow the instructions below:__
* GE-1. Run `geuvadis_extract_data.py` using the vcf file (genotype) and rs id map file (both obtained from gEUVADIS portal) as input.
* GE-2. Create an SQL database using gEUVADIS gene expression data. (cols: sampleid, gene_id, gene_exp)
* GE-3. Run `geuvadis_genotype_expression_by_sample.py` using GE-1 and CG-2 outputs as input. Also name the path were the output files will be saved.
* GE-4. Run `geuvadis_eqtl.py` using the directory path of GE-3 output files as input.

__To generate the GTEx analysis (step 2 of paper workflow), please follow the following instructions below:__
* GT-1. Run `gtex_overlap.py` using CG-2 output and GTEx significant eQTL files path as input. Also name the path were the output files will be saved.

__To generate the clinical/pharmacological analysis (step 3 of paper workflow), please follow the following instructions below:__
* CP-1. Run `gwas_overlap.py` using the GE-3 (gEUVADIS) or GT-1 (GTEx) output files as input.
* CP-2. Run `pharmgkb_overlap.py` using the GE-3 (gEUVADIS) or GT-1 (GTEx) output files as input.

__To generate the association networks analysis (step 3 of paper workflow), CP-1 and CP-2 output files were imported to Cytoscape (referenced in the paper) software.__
