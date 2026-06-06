def read_fasta(filename):
    sequence = {}
    current_header = ""
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                current_header = line
                sequence[current_header] = ""
            else:
                if current_header:
                    sequence[current_header] += line.upper()
    return sequence                
    
def gc_counter(sequence):
    count_G = sequence.count('G')
    count_C = sequence.count('C')
    if len(sequence) == 0:
        return 0
    GC = ((count_G + count_C)/len(sequence))*100
    print("GC content:", GC,'%')

def rebuild_reverse_complement(sequence):
    i = 0
    complement = ""
    while(i < len(sequence)):
        if(sequence[i] == "A"):
            complement += "T"
        elif(sequence[i] == "T"):
            complement += "A"
        elif(sequence[i] == "C"):
            complement += "G"
        elif(sequence[i] == "G"):
            complement += "C"
        i += 1
    rev_complement = complement[::-1]
    print("Reverse complement:", rev_complement)
    
def nucleotide_counter(sequence):
    print("Length of nucleotide:", len(sequence))
    print("A:", sequence.count('A'), (sequence.count('A')/len(sequence)*100))
    print("T:", sequence.count('T'), (sequence.count('T')/len(sequence)*100))
    print("G:", sequence.count('G'), (sequence.count('G')/len(sequence)*100))
    print("C:", sequence.count('C'), (sequence.count('C')/len(sequence)*100))
 
def mutation_detector(sequence):
    sequence_list = list(sequence.values())
    if ( len(sequence_list) < 2 ):
        print("You need at least 2 sequence to compare!")
        return
    reference = sequence_list[0]
    print(f"Reference sequence (#Seq 1): {reference}")
    seq_num = 2
    for current_sequence in sequence_list[1:]:
        print(f"Comparing sequence #{seq_num}: {current_sequence}")
        i = 0
        mutation_count = 0
        while i < min(len(reference), len(current_sequence)):
            if reference[i] != current_sequence[i]:
                mutation_count += 1
                print(f"Mutation found at position {i+1}: Reference had {reference[i]}, but this sequence has '{current_sequence[i]}'")
            i += 1
        print(f"Total mutaion found in sequence #{seq_num}: {mutation_count}")
        seq_num += 1
    
fasta_data = read_fasta("Fasta.txt")
for headers, dna_strand in fasta_data.items():
    print(f"\nHeader: {headers}")
    gc_counter(dna_strand)
    rebuild_reverse_complement(dna_strand)
    nucleotide_counter(dna_strand)
    
print(fasta_data)
mutation_detector(fasta_data)