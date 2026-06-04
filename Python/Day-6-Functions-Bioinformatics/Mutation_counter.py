dna1 = input("Enter the first sequence: ")
dna2 = input("Enter the first sequence: ")
i=0
count = 0
while(i < len(dna1) and i < len(dna2)):
    if(dna1[i] != dna2[i]):
        count += 1
        print((f'position {i}:') ,dna1[i],'->', dna2[i]  )
    i += 1
print("No. of mutation sites:", count)
