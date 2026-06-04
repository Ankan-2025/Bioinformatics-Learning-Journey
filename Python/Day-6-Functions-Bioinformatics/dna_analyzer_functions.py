def count_nucleotide(dna):
    print("Length of DNA sequence: ", len(dna))
    return 

def GC_count(dna):
    count_G = dna.count('G')
    count_C = dna.count('C')
    GC = ((count_G + count_C)/len(dna))*100
    print("GC% = ", round(GC))
    return

def reverse_complement(dna):
    i = 0
    complement = ""
    while( i < len(dna)):
        if( dna[i] == "A"):
            complement += "T"
        elif( dna[i] == "T"):
            complement += "A"
        elif( dna[i] == "G"):
            complement += "C"
        elif( dna[i] == "C"):
            complement += "G"
        i += 1
    A = complement[::-1]
    print("Reverse complement:", A)

def validation(dna):
    for bases in dna:
        if( bases not in ('A', 'T', 'G', 'C')):
            print("Invalid DNA sequence")
            return False
    print("Valid")
    return True
        
dna_sequence = input("Enter the DNA sequence: ")
count_nucleotide(dna_sequence)
GC_count(dna_sequence)
reverse_complement(dna_sequence)
validation(dna_sequence)
