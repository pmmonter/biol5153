#!/bin/sh
#Paola Monterroso Diaz
#BIOL5153
#Spring 2020
#
#assn01-1
cd ~ ;find . -iname 'nad*'
#
#ass01-2
top
#command 'top' was used
#3.5% of CPU was being used by this command
#PhysMem: 5819M used (1582M wired), 2372M unused
#
#assn01-3
cd ~/Desktop/watermelon_files; grep 'misc_feature' watermelon.gff | sort -n -k7 -r > 'IR_regions.gff'
#
#assn01-4
grep -c 'misc_feature' watermelon.gff ; grep -vc 'misc_feature' watermelon.gff
#No, it is not the case. More chloroplast fragments come from outside the IR than inside. 
#
#assn01-5
cd ~/Desktop/watermelon_files; grep -v 'GAATTC' genes.fsa | grep -B 1 'GGATCC'
#
#assn01-6
cd ~/Desktop/example_files; head -n 1001 shaver_etal.csv | tail -n 501
#
#assn01-7
cd ~/Desktop/example_files; column -t fruit.txt | sort -k2r | sort -k3


