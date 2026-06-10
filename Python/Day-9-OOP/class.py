class DNASequence:
    def __init__(self, sequence):
        self.sequence = sequence
        self.length = len(sequence)

    def show_sequence(self):
        print(f"DNA Sequence: {self.sequence}")
    def get_length(self):
        return self.length
    def gc_content(self):
        count_G = self.sequence.count('G')
        count_C = self.sequence.count('C')
        if self.length == 0:
            return 0
        GC = ((count_G + count_C)/self.length)*100
        return GC
    def reverse_complement(self):
        i = 0
        complement = ""
        while(i < self.length):
            if(self.sequence[i] == "A"):
                complement += "T"
            elif(self.sequence[i] == "T"):
                complement += "A"
            elif(self.sequence[i] == "C"):
                complement += "G"
            elif(self.sequence[i] == "G"):
                complement += "C"
            i += 1
        reverse = complement[::-1]
        return reverse
        
human = DNASequence("ATGCGTAC")
human.show_sequence()
print("Human Data")
print(f"Sequence length: {human.get_length()}")
print("GC content:",human.gc_content(),'%')
print("Reverse Complement:", human.reverse_complement())
print("\nMouse Data")
mouse = DNASequence("ATGAGTTC")
print(f"Sequence length: {mouse.get_length()}")
print("GC content:",mouse.gc_content(),'%')
print("Reverse Complement:", mouse.reverse_complement())
print("\nVirsu Data")
virus = DNASequence("ATGCGTAA")
print(f"Sequence length: {virus.get_length()}")
print("GC content:",virus.gc_content(),'%')
print("Reverse Complement:", virus.reverse_complement())