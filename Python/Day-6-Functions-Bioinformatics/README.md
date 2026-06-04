# Day 6 - Functions & Recursion 🐍🧬

## Topics Learned
- Function definition & calling
- Parameters & arguments
- Return values
- Default parameters
- Recursion & base case

---

## Bioinformatics Connection 🔬

| Python Concept | Bioinformatics Use |
|----------------|-------------------|
| `def function()` | Reusable sequence analysis tools |
| Parameters | Pass any DNA sequence to analyze |
| Return values | Get GC%, length, complement back |
| Recursion | Recursive traversal of biological sequences |
| Validation function | Ensure sequence quality before analysis |

---

## Practice Problems

### 🧬 Bioinformatics Problems
1. DNA Analyzer using Functions — length, GC%, reverse complement, validation
2. Finding Maximum GC% across multiple sequences
3. Mutation Counter — compare two DNA sequences (Hamming Distance)
4. Nucleotide Counter using Recursion

### 🐍 Python Problems
5. Print list length using function
6. Print list elements using function
7. Factorial using function
8. USD to INR converter
9. Sum of n natural numbers using recursion
10. Print list elements using recursion

---

## Example — DNA Analyzer with Functions
```python
def GC_count(dna):
    count_G = dna.count('G')
    count_C = dna.count('C')
    GC = ((count_G + count_C) / len(dna)) * 100
    print("GC% =", round(GC))

def validation(dna):
    for base in dna:
        if base not in ('A', 'T', 'G', 'C'):
            print("Invalid DNA sequence")
            return False
    print("Valid")
    return True
```

---

## Highlight — Mutation Counter 🔥
```python
# Compares two DNA sequences and finds mutation positions
# This is the Hamming Distance algorithm used in genomics
# to measure genetic distance between sequences
while i < len(dna1) and i < len(dna2):
    if dna1[i] != dna2[i]:
        print(f'Position {i}: {dna1[i]} -> {dna2[i]}')
```

---

## What This Means Biologically 🔬
Functions are the foundation of reusable bioinformatics tools.
Every tool in the bioinformatics ecosystem — BLAST, Biopython,
genome browsers — is built from modular functions.

The Mutation Counter built today is essentially the
**Hamming Distance algorithm** used to measure genetic
differences between DNA sequences — a core concept in
evolutionary biology and genomics.

---

## FreeCodeCamp Progress 🎯
- ✅ Bill Splitter Workshop (complete)
- ✅ Movie Ticket Booking Calculator Workshop (complete)

🔗 [FreeCodeCamp Python Certification](https://www.freecodecamp.org/learn/python-v9/)

---

## Future Improvements 🚀
- Add stop codon detection to DNA analyzer
- Build multi-sequence alignment using functions
- Apply Hamming Distance to real mutation datasets
- Refactor Day 5 DNA Analyzer using functions

---

## Learning Resources
- 📺 [Lecture 6 : Functions & Recursion in Python | Apna College](https://www.youtube.com/watch?v=OvTH-7ESoRA&list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0&index=6)
- 🌐 [FreeCodeCamp Python Certification](https://www.freecodecamp.org/learn/python-v9/)

---

## Notes
[Lecture6_py.pdf](https://drive.google.com/file/d/1t_HLGrRMfMpQqC8ivJgGXBTL-AqQA8gw/view?usp=drive_link)

---
## 📈 Computational Workflow

```text
DNA Sequence
      ↓
Validation Function
      ↓
GC% Analysis
      ↓
Reverse Complement
      ↓
Mutation Comparison
      ↓
Recursive Traversal
      ↓
Sequence Analysis Output
```

## Goal
Build reusable, modular bioinformatics functions
that can be combined into complete analysis pipelines. 🧬
