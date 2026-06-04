user_inputs = []
print("Enter the sequences (type 'done' to stop): ")
while True:
    sequence = input("> ")
    if sequence.lower() == 'done':
        break
    user_inputs.append(sequence)

def GC_counter(dna):
    i=0
    count_G = 0
    count_C = 0
    while( i < len(dna)):
        if( dna[i] == 'G'):
            count_G += 1
        elif( dna[i] == "C"):
            count_C += 1
        i += 1
    GC = ((count_G + count_C)/len(dna))*100
    return GC

gc_results = [GC_counter(sequence) for sequence in user_inputs]
largest_gc = max(gc_results)
sequence_number = gc_results.index(largest_gc) + 1
print(f'Sequence {sequence_number}', 'has highest GC content:', largest_gc,"%")
