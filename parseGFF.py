# /usr/bin/env python3

import argparse
import csv
from Bio import SeqIO

# create an argument parser object
parser = argparse.ArgumentParser(description = "This script parses a GFF file and does stuff with it")

# add positional arguments
parser.add_argument("gff", help="name of the GFF file")
parser.add_argument("fasta", help="name of the FASTA file")

# parse the arguments
args = parser.parse_args()

# read and parse the FASTA file
genome = SeqIO.read(args.fasta, 'fasta')

# read GFF file, line by line
with open(args.gff, 'r') as gff_file:
	
	# create a csv reader object
	reader = csv.reader(gff_file, delimiter="\t")

	for line in reader:
		# skip blank lines
		if not line:
			continue
		else:
			feature = line[2]
			
			# test whether this is a CDS feature
			if feature == 'CDS':
				start = line[3]
                                end   = line[4]
				
				# extract corresponding substring/sequence
				sequence_aux = genome.seq[int(start):int(end)]
				seq_len = len(sequence_aux)
				GC_count = sequence_aux.count('C')+sequence_aux.count('G')
				GC_percent = (GC_count/seq_len)*100
				
				print("GC content:","%.2f"%GC_percent+"%")
