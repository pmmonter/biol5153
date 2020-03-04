#! /usr/bin/env python3
# BIOL 5153
# In class assignment
# 3/2/2020

filename = "dna.txt"
infile = open(filename, 'r')
dna_sequence = infile.read()
infile.close()

seq_len = len(dna_sequence)
dna_sequence_upper=dna_sequence.upper()

a_count = dna_sequence_upper.count('A')
t_count = dna_sequence_upper.count('T')
c_count = dna_sequence_upper.count('C')
g_count = dna_sequence_upper.count('G')

a_percent = (a_count/seq_len)*100
t_percent = (t_count/seq_len)*100
c_percent = (c_count/seq_len)*100
g_percent = (g_count/seq_len)*100

print("Percent A:", "%.2f"%a_percent+"%")
print("Percent T:", "%.2f"%t_percent+"%")
print("Percent C:", "%.2f"%c_percent+"%")
print("Percent G:", "%.2f"%g_percent+"%")
