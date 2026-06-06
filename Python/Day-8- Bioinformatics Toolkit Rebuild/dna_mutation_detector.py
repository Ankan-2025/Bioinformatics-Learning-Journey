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
                sequence[current_header] =""
            else:
                if current_header:
                    sequence[current_header] += line.upper()
    return sequence

def dna_mutation_detector(fasta_dict):
    sequence_list = list(fasta_dict.values())
    if(len(sequence_list) < 2):
        print("You need at least 2 sequence to comapre!")
        return
    reference = sequence_list[0]
    print(f"Reference Sequence (Seq #1): {reference}")

    seq_num = 2
    for current_seq in sequence_list[1:]:
        print(f"Comparing Sequence #{seq_num}: {current_seq}")

        i=0
        mutation_count = 0
        while i < min(len(reference), len(current_seq)):
            if reference[i] != current_seq[i]:
                mutation_count += 1
                print(f"Mutation found at position {i+1}: Reference had '{reference[i]}', but this sequence has '{current_seq[i]}'")
            i += 1
        print(f"Total mutation found in Sequence #{seq_num}: {mutation_count}")
        seq_num += 1

fasta_data = read_fasta("Fasta.txt")
print(fasta_data)
dna_mutation_detector(fasta_data)