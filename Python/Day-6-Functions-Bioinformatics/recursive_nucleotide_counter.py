def count_nucleotide(dna):
    if( dna == ""):
        return 0
    return 1 + count_nucleotide(dna[1:])

total_length = count_nucleotide('GCAT')
print("Length of DNA sequence:", total_length)
