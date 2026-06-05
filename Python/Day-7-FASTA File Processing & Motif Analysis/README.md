# Day 7 - FASTA File Processing & Motif Analysis 🧬🐍

## 📌 Project Overview

Today I worked with real bioinformatics-style sequence files using Python and Linux.
This project focuses on reading FASTA-formatted DNA sequences and performing sequence analysis, calculating GC content, generating reverse complements, and identifying biologically important motifs inside genomic sequences.

This project marks an important transition from learning Python syntax to building practical computational biology workflows using the Linux terminal.

---

## 🛠️ Technologies Used

* Python
* Linux / Bash (WSL2 Ubuntu)
* VS Code
* Nano Text Editor
* File Handling in Python
* FASTA File Processing

---

## 📚 Topics Learned

* File Handling (`open`, `read`, `with`)
* Reading FASTA files
* Sequence parsing
* Functions & modular programming
* Dictionaries in Python
* Motif searching algorithms
* Linux terminal workflow
* Debugging Python errors

---

## 🧬 FASTA File Example

```text
>Human_BRCA1
ATGCGTACCGTA

>Mouse_TP53
GGGTTTAAACC

>Virus_X
ATGAAATTTGGG
```

---

## 🔬 Bioinformatics Features Implemented

### ✅ FASTA Reader

Reads biological sequence files and separates:

* Sequence headers
* DNA sequences

---

### ✅ GC Content Calculator

Calculates:

* Number of `G` and `C` nucleotides
* GC percentage of each sequence

---

### ✅ Sequence Length Analyzer

Determines:

* Total nucleotide length of DNA sequences

---

### ✅ Reverse Complement Generator

Generates:

* Complementary DNA strand
* Reverse-complement sequence

---

### ✅ Motif Finder

Searches biologically important motifs like:

* `ATG` → Start codon
* `GGG`
* `TATA`

and returns their exact starting positions.

---

## 🧪 Example Outputs

```bash
>Human_BRCA1
Motif 'ATG' found at starting indices: [0]

>Mouse_TP53
Motif 'GGG' found at starting indices: [0]

>Virus_X
Motif 'ATG' found at starting indices: [0]
Motif 'GGG' found at starting indices: [9]
```

---

## 🐧 Linux Workflow & Terminal Output

```bash
ankan_bioinfo@layy:~$ mkdir bio_project
ankan_bioinfo@layy:~$ cd bio_project

ankan_bioinfo@layy:~/bio_project$ nano FASTA.txt

ankan_bioinfo@layy:~/bio_project$ cat FASTA.txt

>Human_BRCA1
ATGCGTACCGTA

>Mouse_TP53
GGGTTTAAACC

>Virus_X
ATGAAATTTGGG

ankan_bioinfo@layy:~/bio_project$ nano analyzer.py

ankan_bioinfo@layy:~/bio_project$ python3 analyzer.py

Header: >Human_BRCA1
Sequence: ATGCGTACCGTA
GC content: 50.0 %

Header: >Mouse_TP53
Sequence: GGGTTTAAACC
GC content: 45.45 %

Header: >Virus_X
Sequence: ATGAAATTTGGG
GC content: 33.33 %

Reverse complement: TACGGTACGCAT
Reverse complement: GGTTTAAACCC
Reverse complement: CCCAAATTTCAT

ankan_bioinfo@layy:~/bio_project$ python3 motif_finder.py

>Human_BRCA1
Motif 'ATG' found at starting indices: [0]

>Mouse_TP53
Motif 'GGG' found at starting indices: [0]

>Virus_X
Motif 'ATG' found at starting indices: [0]
Motif 'GGG' found at starting indices: [9]
```

---

## ⚠️ Debugging Journey

During development, I encountered and fixed several real programming issues:

* `ZeroDivisionError`
* `IndentationError`
* `UnboundLocalError`
* Incorrect Linux path navigation
* File naming mistakes
* Variable scope issues

This strengthened my debugging, logical thinking, and command-line workflow skills.

---

## 🔬 What This Means Biologically

### GC Content

GC-rich DNA regions are generally more thermally stable because:

* `G-C` pairs form 3 hydrogen bonds
* `A-T` pairs form 2 hydrogen bonds

GC analysis is important in:

* PCR primer design
* Genome analysis
* Sequence quality analysis

---

### Motif Analysis

Motifs are recurring biological patterns in DNA that may represent:

* Start codons
* Regulatory elements
* Promoter regions
* Protein binding sites

Motif finding is a foundational concept in genomics and computational biology.

---

## 📈 Computational Workflow

```text
FASTA File
     ↓
Sequence Parsing
     ↓
GC Content Analysis
     ↓
Sequence Length Detection
     ↓
Reverse Complement Generation
     ↓
Motif Identification
     ↓
Biological Sequence Insights
```

---

## 📚 Learning Resources

* 📺 Apna College — File I/O in Python
  https://youtu.be/jU0cndZziO0?si=0_2KUi7Sy_el7gpP

* 🌐 FreeCodeCamp Python Certification
  https://www.freecodecamp.org/learn/python-v9/

---

## 📝 Notes

* `Lecture7_py.pdf`

---

## 🚀 Future Improvements

* Support multiline FASTA sequences
* Add RNA transcription module
* Detect stop codons automatically
* Add mutation comparison between sequences
* Export analysis reports to CSV
* Parse larger real-world genomic datasets
* Improve output formatting and reporting structure

---

## 💡 Reflection

This project improved my understanding of biological sequence processing, Linux-based workflows, debugging, and modular programming in Python. It also introduced me to practical bioinformatics concepts such as motif analysis and FASTA parsing.

The debugging process played a major role in strengthening my computational thinking and helped me better understand how real-world bioinformatics workflows operate.

---

## 🎯 Goal

Build foundational bioinformatics tools capable of processing real biological sequence data using Python, Linux, and computational analysis workflows. 🧬
