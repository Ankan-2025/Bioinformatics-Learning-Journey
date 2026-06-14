def orf_finder(dna_sequence):
    current_pos = 0
    number = 1
    while True:
        start_pos = dna_sequence.find("ATG", current_pos)
        if start_pos == -1:
            break
        found_stop = False
        for i in range(start_pos + 3,len(dna_sequence), 3):
            codon = dna_sequence[i:i+3]
            if codon in ("TAA","TAG","TGA"):
                orf = dna_sequence[start_pos:i+3]
                print(f"ORF {number}:",orf)
                print("Length of ORF:",len(orf))
                number += 1
                current_pos = i+3
                found_stop = True
                break
        if not found_stop:
            current_pos = start_pos + 1

test_dna = "ATGAAATTTGGGTAACCCCCCATGCCCCCCGGGTGA"
orf_finder(test_dna)
