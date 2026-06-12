Day 8 - Linux Genome Lab Project 🐧🧬

📌 Project Overview

Today I simulated a small bioinformatics research environment using Linux command-line tools.

The objective was to create a structured genome repository, manage FASTA sequence files, perform sequence searches, create backups, identify corrupted files, and generate reports entirely from the Linux terminal.

This project strengthened my understanding of how bioinformatics workflows are performed on Linux systems before downstream sequence analysis.

---

🛠️ Technologies Used

- Linux / Bash (WSL2 Ubuntu)
- FASTA Files
- grep
- find
- wc
- cp
- cat
- touch
- echo
- ls
- pwd

---

📚 Concepts Practiced

Linux File Management

- Directory creation
- File creation
- Recursive directory inspection
- Backup workflows

Bioinformatics Operations

- FASTA file organization
- Header searching
- DNA motif searching
- Dataset auditing

Linux Utilities

- "grep"
- "find"
- "wc"
- "cp"
- "cat"
- "ls -R"

Debugging

- Path errors
- Copy command mistakes
- grep syntax issues
- File deletion mistakes

---

🧬 Project Structure

genome_lab/
│
├── human/
│   ├── brca1.fasta
│   └── tp53.fasta
│
├── bacteria/
│   ├── ecoli.fasta
│   └── salmonella.fasta
│
├── virus/
│   └── covid9.fasta
│
├── backup/
│
└── reports/
    ├── corrupted.fasta
    └── summary.txt

---

🐧 Linux Workflow

Create Genome Repository

ankan_bioinfo@layy:~$ mkdir genome_lab
ankan_bioinfo@layy:~$ cd genome_lab

ankan_bioinfo@layy:~/genome_lab$ mkdir human bacteria virus backup reports

Create FASTA Files

ankan_bioinfo@layy:~/genome_lab/human$ touch brca1.fasta tp53.fasta

ankan_bioinfo@layy:~/genome_lab/bacteria$ touch ecoli.fasta salmonella.fasta

ankan_bioinfo@layy:~/genome_lab/virus$ touch covid9.fasta

Add Sequence Data

ankan_bioinfo@layy:~/genome_lab/virus$ echo '>BRCA1_Human' > covid9.fasta
ankan_bioinfo@layy:~/genome_lab/virus$ echo 'ATGCGTACCGTAGGCTA' >> covid9.fasta

Verify Sequence Files

ankan_bioinfo@layy:~/genome_lab/bacteria$ cat salmonella.fasta

>BRCA1_Human
ATGCGTACCGTAGGCTA

Backup All FASTA Files

ankan_bioinfo@layy:~/genome_lab$ cp human/brca1.fasta human/tp53.fasta \
bacteria/ecoli.fasta bacteria/salmonella.fasta \
virus/covid9.fasta backup/

---

🔍 Dataset Inspection

Find All FASTA Headers

ankan_bioinfo@layy:~/genome_lab$ grep -R "^>"

backup/tp53.fasta:>BRCA1_Human
backup/brca1.fasta:>BRCA1_Human
backup/covid9.fasta:>BRCA1_Human
backup/salmonella.fasta:>BRCA1_Human
backup/ecoli.fasta:>BRCA1_Human
human/tp53.fasta:>BRCA1_Human
human/brca1.fasta:>BRCA1_Human
virus/covid9.fasta:>BRCA1_Human
bacteria/salmonella.fasta:>BRCA1_Human
bacteria/ecoli.fasta:>BRCA1_Human

Search for ATG Motifs

ankan_bioinfo@layy:~/genome_lab$ grep -R "ATG"

backup/covid9.fasta:ATGCGTACCGTAGGCTA
backup/salmonella.fasta:ATGCGTACCGTAGGCTA
backup/ecoli.fasta:ATGCGTACCGTAGGCTA
virus/covid9.fasta:ATGCGTACCGTAGGCTA
bacteria/salmonella.fasta:ATGCGTACCGTAGGCTA
bacteria/ecoli.fasta:ATGCGTACCGTAGGCTA

---

🧪 Quality Control & Dataset Audit

Count FASTA Files

ankan_bioinfo@layy:~/genome_lab$ find . -type f -name "*.fasta" | wc -l
10

Count FASTA Headers

ankan_bioinfo@layy:~/genome_lab$ grep -R "^>" | wc -l
10

Count Files Containing ATG

ankan_bioinfo@layy:~/genome_lab$ grep -R "ATG" | wc -l
6

Find Empty FASTA Files

ankan_bioinfo@layy:~/genome_lab/reports$ find . -type f -empty

./corrupted.fasta

Display FASTA File Sizes

ankan_bioinfo@layy:~/genome_lab$ find . -type f -name "*.fasta" -exec ls -lh {} \;

Output:

-rw-r--r-- 1 ankan_bioinfo ankan_bioinfo 31 Jun 12 11:11 ./backup/covid9.fasta
-rw-r--r-- 1 ankan_bioinfo ankan_bioinfo 31 Jun 12 11:11 ./backup/ecoli.fasta
-rw-r--r-- 1 ankan_bioinfo ankan_bioinfo 31 Jun 12 11:11 ./backup/salmonella.fasta
...

---

⚠️ Debugging Journey

Mistake 1

ankan_bioinfo@layy:~/genome_lab/virus$ covid9.fasta

covid9.fasta: command not found

Fix:

touch covid9.fasta

---

Mistake 2

cp: target 'backup/': Not a directory

Fix:

cp human/brca1.fasta human/tp53.fasta bacteria/ecoli.fasta \
bacteria/salmonella.fasta virus/covid9.fasta backup/

---

Mistake 3

grep -R ("^>")

Result:

syntax error near unexpected token '('

Fix:

grep -R "^>"

---

Mistake 4

rm ~genome_lab/human/backup

Result:

No such file or directory

Fix:

rm ~/genome_lab/human/backup

---

🔬 Bioinformatics Relevance

Linux Command| Bioinformatics Use
"grep"| Search DNA motifs and FASTA headers
"find"| Locate genome files
"wc"| Count datasets and records
"cp"| Backup sequencing data
"cat"| Inspect sequence files
"ls -R"| Explore project structure
"find -empty"| Detect corrupted or incomplete files

---

📈 Workflow

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

---

🚀 Future Improvements

- Automate report generation using Bash scripts
- Calculate GC content from terminal
- Build FASTA parsers in Python
- Automate motif searches
- Integrate Linux workflows with Biopython
- Process larger genomics datasets

---

🎯 Goal

Develop strong Linux command-line skills for managing genomic datasets, organizing bioinformatics projects, and preparing biological sequence data for computational analysis and future genomics workflows. 🧬
