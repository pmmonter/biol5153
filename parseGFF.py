# /usr/bin/env python3

# define input file 
infile = "watermelon.gff"
gene = list()

# open and parse watermelon.gff file
with open(infile, 'r') as wm:
    for line in wm:
        fields = line.split()

        # extract gene name and store in list    
        if not fields[10].startswith('simil'):
            gene.append(fields[10])

# sort in alphabetical order and print list
gene.sort()
print(gene)


