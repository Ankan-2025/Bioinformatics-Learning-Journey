# Day 11 - OOP, ORF Finder & Bioinformatics String Analysis 🐍🧬

## 📌 Overview
Day 11 focused on three parallel tracks:
- Strengthening Python OOP with a reusable `DNASequence` class
- Building a Multi-ORF Finder for gene prediction
- Learning bioinformatics-specific Python string operations
  from Bioinformatics Coach

---

## 🧬 DNASequence Class (OOP)

A reusable class for DNA sequence analysis built using
Python OOP concepts.

```python
human = DNASequence("ATGCGTAC")
human.show_sequence()
human.get_length()
human.gc_content()
human.reverse_complement()
```

### Methods Implemented
| Method | Returns |
|--------|---------|
| `show_sequence()` | Prints DNA sequence |
| `get_length()` | Returns sequence length |
| `gc_content()` | Returns GC percentage |
| `reverse_complement()` | Returns reverse complement |

### Sample Output
```text
Human Data
Sequence Length:    8
GC Content:         50.0 %
Reverse Complement: GTACGCAT

Mouse Data
Sequence Length:    8
GC Content:         37.5 %
Reverse Complement: GAACTCAT

Virus Data
Sequence Length:    8
GC Content:         37.5 %
Reverse Complement: TTACGCAT
```

---

## 🔬 Multi-ORF Finder

Detects multiple Open Reading Frames in a DNA sequence.

### Biological Concepts
| Term | Definition |
|------|-----------|
| `ATG` | Start codon — begins translation |
| `TAA`, `TAG`, `TGA` | Stop codons — ends translation |
| ORF | Coding region between start & stop |

### Sample Input & Output
```text
Input:  ATGAAATTTGGGTAACCCCCCATGCCCCCCGGGTGA

ORF 1: ATGAAATTTGGGTAA  → Length: 15
ORF 2: ATGCCCCCCGGGTGA  → Length: 15
```

```text
Input:  CCCCCCCCCCCC
Output: No ORF Found
```

---

## 📚 Bioinformatics Coach — String Analysis

Worked through a dedicated bioinformatics Python tutorial
covering sequence manipulation using Python strings.

### DNA Sequence Exercises
```python
dna_sequence = 'AGTTAGCTAGGAGGTTAGGGACC'

# 1. Nucleotide count
len(dna_sequence)

# 2. GC Content
GC = (dna_sequence.count('G') + dna_sequence.count('C')) / len(dna_sequence) * 100

# 3. Purines (A + G)
dna_sequence.count('G') + dna_sequence.count('A')

# 4. Pyrimidines (C + T)
dna_sequence.count('C') + dna_sequence.count('T')

# 5. Nucleotide at position 10
dna_sequence[9]

# 6. Subsequence position 3 to 9
dna_sequence[2:9]

# 7. Position 10 to end
dna_sequence[9:20]

# 8. Motif search
'GGAGG' in dna_sequence

# 9. TTA occurrence count
dna_sequence.count('TTA')

# 10. GTTA start index
dna_sequence.find('GTTA')

# 11. Contains Z?
dna_sequence.find('Z')
```

### Key Concepts Covered
| Concept | Bioinformatics Use |
|---------|-------------------|
| `.count()` | Nucleotide frequency |
| `.find()` | Motif location |
| `.replace('T','U')` | DNA → RNA conversion |
| `len()` | Sequence length |
| Slicing `[i:j]` | Subsequence extraction |
| Purines (A,G) / Pyrimidines (C,T) | Sequence composition |

---

## 🎯 Key Outcomes
- Built a reusable `DNASequence` class using OOP ✅
- Implemented Multi-ORF Finder with no-ORF detection ✅
- Completed Bioinformatics Coach string analysis tutorial ✅
- Applied 12 biological sequence questions in Python ✅

---

## 🚀 Next Goals
- Add nucleotide percentage calculations to `DNASequence`
- Read sequences directly from FASTA files
- Upgrade ORF Finder to accept FASTA input
- Start exploring Biopython

---

## 🌱 Learning Resources
- 📺 [Python Strings for Bioinformatics | Bioinformatics Coach](https://youtu.be/uJZLZhRhK90?si=d-lxIwfkO2Jvr84_)
