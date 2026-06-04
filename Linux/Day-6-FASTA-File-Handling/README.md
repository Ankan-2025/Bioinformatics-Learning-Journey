# Day 6 - Linux FASTA File Handling 🐧🧬

## Environment
- OS: Windows 11 + WSL2 (Ubuntu)
- Linux user: `ankan_bioinfo`
- Workspace: `/home/ankan_bioinfo/research_project`

---

## Key Discovery Today 🔑
```bash
>  overwrites file content
>> appends to existing file  ← learned through trial & error!
```

---

## Commands Used

| Command | What it does |
|---------|-------------|
| `echo ">" > file` | Write FASTA header to file |
| `echo "seq" >> file` | Append DNA sequence to file |
| `grep "^>"` | Search for FASTA headers |
| `grep -c ">"` | Count sequences in FASTA file |
| `grep -r "ATG"` | Recursive motif search |
| `cat` | Read FASTA file content |

---

## Practice Done — Research Project Setup
```bash
# Created research project structure
mkdir research_project
cd research_project
touch human.fasta virus.fasta bacteria.fasta

# Created proper FASTA format files
echo ">Human_BRCA1" > human.fasta
echo "ATGCGTACCGTA" >> human.fasta

# Searched FASTA headers across all files
grep "^>" human.fasta virus.fasta bacteria.fasta

# Searched for ATG start codon
grep "ATG" human.fasta virus.fasta bacteria.fasta

# Counted sequences per file
grep -c ">" human.fasta virus.fasta bacteria.fasta

# Recursive search across entire project
grep -r "ATG"
```

---

## Errors & Fixes 🔧
```bash
$ echo "ATGCGTACCGTA" > human.fasta
# Error: overwrote the header line!
# Fix: use >> to append instead of >

$ rm ATGCGTACCGTA
# Error: tried to remove sequence as a file
# Fix: rm human.fasta then recreate properly

$ grep "ATG" research_project
# Error: Is a directory
# Fix: grep -r "ATG"  ← recursive flag needed
```

---

## Understanding FASTA Format 🔬
Human_BRCA1        ← header line (starts with >)
ATGCGTACCGTA        ← sequence line

FASTA is the most common file format in bioinformatics.
Used to store DNA, RNA and protein sequences.
Every genome database (NCBI, Ensembl) uses this format.

---

## Bioinformatics Connection 🔬

| Linux Command | Bioinformatics Use |
|--------------|-------------------|
| `grep "^>"` | Count sequences in FASTA file |
| `grep "ATG"` | Find start codons in genome |
| `grep -r` | Search entire genome project |
| `>>` operator | Build multi-sequence FASTA files |

---

## Key Takeaway 💡
Today I created and manipulated real FASTA format files
from the Linux terminal — the same format used in NCBI,
Ensembl and every major genomics database.

The `grep "^>"` pattern is used daily by bioinformaticians
to count sequences and validate FASTA files before analysis.

---

## Learning Resources
- 📺 [Linux Command Line Tutorial For Beginners | ProgrammingKnowledge](https://youtube.com/playlist?list=PLS1QulWo1RIb9WVQGJ_vh-RQusbZgO_As)

---

## Goal
Master Linux file handling for bioinformatics —
creating, editing and searching FASTA sequence files
from the command line. 🧬
