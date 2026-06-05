with open("FASTA.txt") as f:
    for line in f:
        if line.startswith(">"):
            print('Header: ', line.strip())
        else:
            print('Sequence:',line.strip())
        
def gc_counter():
    with open("FASTA.txt", 'r') as f:
        for line in f:
            if line.startswith(">"):
                print('Header: ', line.strip())
            else:
                print('Sequence:',line.strip())
                sequence = line.strip()
                if sequence == "":
                    continue
                i = 0
                count_G = 0
                count_C = 0
                while(i < len(sequence)):
                    if(sequence[i] == "G"):
                        count_G += 1
                    elif(sequence[i] == "C"):
                        count_C += 1
                    i += 1
                GC = ((count_G + count_C)/len(sequence))*100
                print("GC content:",GC,"%")

def sequence_length():
    with open("FASTA.txt", "r") as f:
        for line in f:
            if line.startswith('>'):
                print('Header: ', line.strip())
            else:
                print('Sequence:',line.strip())
                sequence = line.strip()
                if sequence == "":
                    continue
                i = 0
                count = 0
                while(i < len(sequence)):
                    count += 1
                    i += 1
                print("Length of DNA sequence:", count)

def reverse_complement():
    with open("FASTA.txt", "r") as f:
        for line in f:
            if line.startswith('>'):
                print('Header: ', line.strip())
            else:
                print('Sequence:',line.strip())
                sequence = line.strip()
                if sequence == "":
                    continue
                i = 0
                complement = ""
                while( i < len(sequence)):
                    if(sequence[i] == 'A'):
                        complement += 'T'
                    elif(sequence[i] == 'T'):
                        complement += 'A'
                    elif(sequence[i] == 'G'):
                        complement += 'C'
                    elif(sequence[i] == 'C'):
                        complement += 'G'
                    i += 1
                reverse = complement[::-1]
                print("Reverse complement:", reverse)
gc_counter()
sequence_length()
reverse_complement()