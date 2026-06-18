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

def report_generator():
    total_bp = 0
    longest_length = 0
    longest_header =""
    fasta_data = read_fasta('Fasta.txt')
    print(f"Total Sequence: ",len(fasta_data))
    for header, dna_strand in fasta_data.items():
        total_bp  += len(dna_strand)
        print(f"{header} Length: {len(dna_strand)}")
        if (len(dna_strand) > longest_length):
            longest_length = len(dna_strand)
            longest_header = header 
    print(f"Longest Sequence: {longest_header}")
    print(f"Length : {longest_length}")
    print(f"Total Nucleotide: {total_bp} ")

def orf_finder(dna_sequence):
    current_pos = 0
    number = 1
    orf_found = False
    while True:
        start_pos = dna_sequence.find("ATG", current_pos)
        if start_pos == -1:
            break
        found_stop = False
        for i in range(start_pos + 3,len(dna_sequence), 3):
            codon = dna_sequence[i:i+3]
            if codon in ("TAA","TAG","TGA"):
                orf_found = True
                orf = dna_sequence[start_pos:i+3]
                print(f"ORF {number}:",orf)
                print("Length of ORF:",len(orf))
                number += 1
                current_pos = i+3
                found_stop = True
                break
        if not found_stop:
            current_pos = start_pos + 1
    if not orf_found:
        print("No ORF found")
    
fasta_data = read_fasta("Fasta.txt")
for headers, dna_strand in fasta_data.items():
    print(f"\nHeader: {headers}")
    gc_counter(dna_strand)
    rebuild_reverse_complement(dna_strand)
    nucleotide_counter(dna_strand)
    print(f"\nAnalyzing: {headers}")
    orf_finder(dna_strand)
print(fasta_data)
mutation_detector(fasta_data)
report_generator()