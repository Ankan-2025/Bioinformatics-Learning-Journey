# Day 2 - Strings & Conditional Statements 🐍🧬

## Topics Learned
- Strings & String Operations
- Indexing & Slicing
- Negative Indexing
- String Functions (count, find, replace, capitalize, endswith)
- Conditional Statements (if-elif-else)

## Bioinformatics Connection 🔬
String methods are the foundation of DNA sequence analysis:

| Python Method | Bioinformatics Use |
|---------------|-------------------|
| `.count()` | Count nucleotides (A, T, G, C) |
| `.find()` | Locate start codon (ATG) |
| `slicing [0:3]` | Extract codons from sequence |
| `len()` | Measure sequence length |

## Practice Problems

### 🧬 Bioinformatics Problems
1. GC Content Analysis of a DNA sequence
2. DNA Sequence Analyzer (nucleotide counter + start codon finder)

### 🐍 Python Problems
3. Name length finder
4. Occurrence of '$' in a string
5. Odd or Even checker
6. Greatest of 3 numbers
7. Multiple of 7 checker

## Example — GC Content
```python
DNA = "ATGCGTACCGTA"
GC_content = ((DNA.count("G") + DNA.count("C")) / len(DNA)) * 100
print("GC Content %:", round(GC_content, 2))  # Output: 50.0
```

## What This Means Biologically
GC content tells us the thermal stability of a DNA sequence.
High GC content = more stable DNA = important in PCR primer design
and genome analysis. This is one of the first calculations in
real bioinformatics pipelines. 🔬

## Learning Resources
- 📺 [Lecture 2 : Strings & Conditional Statements | Apna College](https://youtu.be/lIId8IDP6TU?si=wc54Ker2TBGyla0Q)
- https://www.freecodecamp.org/learn/python-v9/

## Notes
[Lecture2_py.pdf](https://drive.google.com/file/d/1BZrY3j7aXLxI2uuXV6BBmpNN0MsPjN-v/view?usp=drive_link)

## Goal
Apply every Python string concept directly
to biological sequences and DNA analysis. 🧬
