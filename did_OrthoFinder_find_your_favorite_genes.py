#Did recipricol-best-hits or OrthoFinder find your favorite genes?
#Sian Bray 2nd July 2019

import argparse

parser=argparse.ArgumentParser(description="Add gene descriptions to recipricol-best-hits or ortholouge groups. Defaults are set to use the output orthogroups.tsv from OrthoFinder.")
parser.add_argument('-f', type=str, metavar='input_favorite_genes_list', required=True, help='Path to the tab deliminated file containing a list of your favorite genes.')
parser.add_argument('-r', type=str, metavar='rbh_file', required=True, help='Path to your reciprocol-best-hit or orthogroup output.')
parser.add_argument('-o', type=str, metavar='output_file', required=True, help='Name and/or path for the output file.')
parser.add_argument('-c', type=int, metavar='column', required=False, default=0, help='The column in your favorite gene list that contains the gene names of the reference organisms (from which the annotation comes).')
args=parser.parse_args()

favorite_genes=open(args.f, 'r')
output_file=open(args.o, 'w+')

for count0, line in enumerate(favorite_genes):
	split_line=line.replace('\n', '')
	split_line=split_line.split('\t')
	gene=split_line[args.c]
	output_file.write(line.replace('\n', ''))
	rbh_output=open(args.r, 'r')
	any_genes=False
	for count2, line2 in enumerate(rbh_output):
		if gene in line2:
			output_file.write('\tFound.')
			any_genes=True
	if any_genes==False:
		output_file.write('\tNot found.')
	rbh_output.close()
	output_file.write('\n')

favorite_genes.close()
output_file.close()
