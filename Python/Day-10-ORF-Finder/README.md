# Day 10 - ORF Finder & Gene Prediction 🐍🧬

## 📌 Overview
Today I built my first genomics-oriented bioinformatics project —
an Open Reading Frame (ORF) Finder.

After completing Python fundamentals and OOP, this project
introduced biological concepts directly related to gene prediction.

---

## 🧬 What is an ORF?
An Open Reading Frame is a region of DNA that begins with
a start codon and ends with a stop codon.

```text
ATG | AAA | TTT | GGG | TAA
 ↑                       ↑
Start                   Stop
```

Everything between start and stop = potential protein-coding region.

---

## 📚 Biological Concepts Learned

| Concept | Meaning |
|---------|---------|
| `ATG` | Start codon — begins translation |
| `TAA`, `TAG`, `TGA` | Stop codons — ends translation |
| Codon | Group of 3 nucleotides |
| ORF | Coding region between start & stop |
| Reading Frame | DNA read in triplets from ATG |

---

## 🚀 Project 1 — Basic ORF Finder

**Input:**
```text
ATGAAATTTGGGTAA
```

**Output:**
```text
ORF 1: ATGAAATTTGGGTAA
Length of ORF: 15
```

---

## 🚀 Project 2 — Multi-ORF Finder

**Input:**
```text
ATGAAATTTGGGTAACCCCCCATGCCCCCCGGGTGA
```

**Output:**
```text
ORF 1: ATGAAATTTGGGTAA
Length of ORF: 15

ORF 2: ATGCCCCCCGGGTGA
Length of ORF: 15
```

## 🧠 Logic Workflow
```text
Scan DNA Sequence
        ↓
Find ATG (Start Codon)
        ↓
Read codons in triplets
        ↓
Find Stop Codon (TAA/TAG/TGA)
        ↓
Extract ORF
        ↓
Continue Searching
        ↓
Find Additional ORFs
```

---

## ⚠️ Challenges Faced

**Reading Frame Confusion:**
```text
# Correct — read in triplets from ATG:
ATG | AAA | TTT | GGG | TAA  ✅

# Wrong — shifted reading frame:
TGA | AAT | TTG ...           ❌
```

**Key insight:**
```python
# This single line ensures correct reading frame:
range(start_pos + 3, len(dna_sequence), 3)
# Starts after ATG, moves in steps of 3
```

---

## 🔬 Why This Matters
ORF detection is a foundational step in genomics.

Real gene prediction tools like **Augustus** and **GeneMark**
use exactly this logic at their core:

```text
Start Codon Detection
        ↓
Coding Region Extraction
        ↓
Stop Codon Detection
        ↓
Protein Translation
        ↓
Genome Annotation
```

---

## 📈 Skills Used
### Python
✅ Functions & Loops
✅ String Methods (`.find()`, slicing)
✅ Nested Loops
✅ Boolean Flags

### Bioinformatics
✅ Start & Stop Codon Detection
✅ Reading Frame Awareness
✅ ORF Extraction
✅ Gene Prediction Concepts

---

## 🚀 Future Improvements
- Read sequences directly from FASTA files
- Detect ORFs in multiple sequences
- Translate ORFs into amino acid sequences
- Identify the longest ORF
- Generate ORF analysis reports

---

## 🌱 Learning Resources
- 📺 [Lecture 8 : OOP in Python | Apna College](https://youtu.be/bAwmZVJeO5s?si=eFrtqKZzp7OE7SZ_)
- 🌐 [FreeCodeCamp Python Certification](https://www.freecodecamp.org/learn/python-v9/)

---

## 🏆 Day 10 Outcome
Built a functional ORF Finder that correctly identifies
multiple protein-coding regions in a DNA sequence —
my first real step into computational gene prediction. 🧬🚀
