rna = {'G': 'G --> C', 'C': 'C --> G', 'T': 'T --> A', 'A': 'A --> U'}

dna = input('Enter dna nucleotide: ')

for x, y in rna.items():
    if dna.upper() == x:
        print (rna[x])