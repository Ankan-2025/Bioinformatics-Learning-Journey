# Day 8 - Linux Genome Lab Project 🐧🧬

## 📌 Project Overview

Today I simulated a small bioinformatics research environment using Linux command-line tools.

The objective was to create a structured genome repository, manage FASTA sequence files, perform motif searches, create backups, identify corrupted files, and audit biological datasets directly from the Linux terminal.

This project helped me understand how bioinformatics workflows are organized and managed before downstream sequence analysis.

---

## 🛠️ Technologies Used

- Linux / Bash (WSL2 Ubuntu)
- FASTA Files
- grep
- find
- wc
- cp
- cat
- touch
- echo

---

## 📚 Concepts Practiced

### Linux Skills

- Directory management
- File creation
- File backups
- Dataset auditing
- Command-line troubleshooting

### Bioinformatics Skills

- FASTA file handling
- Sequence storage
- Header searching
- Motif searching
- Quality control checks

---

## 🧬 Project Structure

```text
genome_lab/
├── human/
│   ├── brca1.fasta
│   └── tp53.fasta
├── bacteria/
│   ├── ecoli.fasta
│   └── salmonella.fasta
├── virus/
│   └── covid9.fasta
├── backup/
└── reports/
    ├── corrupted.fasta
    └── summary.txt
```

---

## 🐧 Linux Workflow

### Create Genome Repository

```bash
mkdir genome_lab
cd genome_lab

mkdir human bacteria virus backup reports
```

### Create FASTA Files

```bash
touch human/brca1.fasta human/tp53.fasta

touch bacteria/ecoli.fasta bacteria/salmonella.fasta

touch virus/covid9.fasta
```

### Add Sequence Data

```bash
echo '>BRCA1_Human' > human/brca1.fasta
echo 'ATGCGTACCGTAGGCTA' >> human/brca1.fasta
```

### Verify File Content

```bash
cat human/brca1.fasta
```

Output:

```text
>BRCA1_Human
ATGCGTACCGTAGGCTA
```

### Create Backup Copies

```bash
cp human/brca1.fasta human/tp53.fasta \
bacteria/ecoli.fasta bacteria/salmonella.fasta \
virus/covid9.fasta backup/
```

---

## 🔍 Dataset Inspection

### Find FASTA Headers

```bash
grep -R "^>"
```

Example Output:

```text
backup/brca1.fasta:>BRCA1_Human
human/brca1.fasta:>BRCA1_Human
virus/covid9.fasta:>BRCA1_Human
...
```

### Search for ATG Motifs

```bash
grep -R "ATG"
```

Example Output:

```text
backup/covid9.fasta:ATGCGTACCGTAGGCTA
virus/covid9.fasta:ATGCGTACCGTAGGCTA
bacteria/ecoli.fasta:ATGCGTACCGTAGGCTA
...
```

---

## 🧪 Quality Control & Dataset Audit

### Count FASTA Files

```bash
find . -type f -name "*.fasta" | wc -l
```

### Count FASTA Headers

```bash
grep -R "^>" | wc -l
```

### Count Files Containing ATG

```bash
grep -R "ATG" | wc -l
```

### Find Empty FASTA Files

```bash
find . -type f -empty
```

Output:

```text
./reports/corrupted.fasta
```

### Display FASTA File Sizes

```bash
find . -type f -name "*.fasta" -exec ls -lh {} \;
```

---

## ⚠️ Debugging Journey

### Mistake 1

```bash
covid9.fasta
```

Output:

```text
command not found
```

Fix:

```bash
touch covid9.fasta
```

### Mistake 2

```bash
grep -R ("^>")
```

Output:

```text
syntax error near unexpected token '('
```

Fix:

```bash
grep -R "^>"
```

### Mistake 3

```bash
rm ~genome_lab/human/backup
```

Output:

```text
No such file or directory
```

Fix:

```bash
rm ~/genome_lab/human/backup
```

---

## 🔬 Bioinformatics Relevance

| Linux Command | Bioinformatics Use |
|--------------|-------------------|
| `grep` | Search DNA motifs and FASTA headers |
| `find` | Locate genome files |
| `wc` | Count datasets and records |
| `cp` | Backup sequencing data |
| `cat` | Inspect sequence files |
| `find -empty` | Detect corrupted or incomplete files |

---

## 📈 Workflow

```text
Create Genome Repository
          ↓
Generate FASTA Files
          ↓
Store DNA Sequences
          ↓
Create Backups
          ↓
Search Headers & Motifs
          ↓
Quality Control Checks
          ↓
Dataset Audit
```

---

## 🚀 Future Improvements

- Automate report generation using Bash scripts
- Build FASTA parsers in Python
- Calculate GC content automatically
- Search biological motifs using Python
- Integrate Linux workflows with Biopython
- Analyze larger genomic datasets

---

## 🎯 Goal

Develop strong Linux command-line skills for managing genomic datasets, organizing bioinformatics projects, and preparing biological sequence data for computational analysis and future genomics workflows. 🧬
