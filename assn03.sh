#! /bin/bash
# Assignment 03
# Paola Monterroso Diaz
# BIOL5153
# Spring 2020

# assn03-1
# for I in {808..8008}
# do
# echo “TR-$i” 
# done

# assn03-2
# alias l=‘ls -al’
# alias h=‘history’

# assn03-3
# cd Desktop/gene_trees
# ls | grep -c ‘\.fasta’
# There are 15085 FASTA files

# assn03-4
# cd Desktop/gene_trees
# ls | grep -c ‘\.tre’
# There are 14640 phylogenetic trees

# assn03-5
# cd Desktop/gene_trees
# ls | grep -c ‘\.sched’
# 15262 analyses have been run

# assn03-6
# cd Desktop/gene_trees
# counter=0
# for f in *.fasta
# do
# fn1=${f:0:19}
# fn2="${fn1}_raxml.tre"
# lines=$(find . -type f -name $fn2 | wc -l)
#	if [ $lines -eq 0  ]
#	then
#		echo "file NOT found for $fn1 FASTA file"
#		counter=$((counter+1));
#	fi
# end
# There is a total of 445 FASTA files with no corresponding tree file

