def read_fasta(filename):
    sequence = {}
    current_header = ""
    with open (filename, "r") as f:
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

def find_exact_motifs(dna,motifs):
    result={}
    for motif in motifs:
        position = []
        start_index = dna.find(motif)
        while start_index != -1:
            position.append(start_index)
            start_index = dna.find(motif, start_index + 1)
            result[motif] = position
    return result
        
motifs = ["ATG", "GGG", "TATA"]
data = read_fasta("FASTA.txt")
data = read_fasta("FASTA.txt")
for header, dna in data.items():

print(header)
matches = find_exact_motifs(dna, motifs)
for motif, positions in matches.items():
print(f"Motif '{motif}' found at starting indices: {positions}")