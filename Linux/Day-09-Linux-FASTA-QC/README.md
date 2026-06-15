# Day 9 - Linux FASTA Quality Control (QC) 🐧🧬

## 📌 Project Overview

Today I simulated a basic bioinformatics quality-control (QC) workflow using Linux command-line tools.

The goal was to identify problematic FASTA files before downstream sequence analysis. I created valid DNA sequence files, intentionally generated corrupted datasets, searched for ambiguous nucleotides (`N`), detected empty FASTA files, generated a QC report, and quarantined problematic files.

This project demonstrates how Linux is used in bioinformatics to perform data validation and quality checks before genome analysis.

---

## 🛠️ Technologies Used

- Linux / Bash (WSL2 Ubuntu)
- FASTA Files
- grep
- find
- wc
- mv
- cat
- touch
- echo

---

## 📚 Concepts Practiced

### Linux Skills
- Directory management
- File creation
- File inspection
- Dataset auditing
- Report generation
- Troubleshooting command-line errors

### Bioinformatics Skills
- FASTA Quality Control
- Detection of ambiguous nucleotides
- Empty file identification
- Dataset validation
- Quarantine workflow

---

## 🧬 Project Structure

```text
genome_lab/
├── good_sequence/
│   ├── sample1.fasta
│   ├── sample2.fasta
│   └── sample3.fasta
│
├── bad_sequence/
│   ├── corrupted1.fasta
│   └── corrupted2.fasta
│
├── quarantine/
│   ├── corrupted1.fasta
│   └── corrupted2.fasta
│
└── reports/
    └── day11_summary.txt
```

---

## 🐧 Linux Workflow

### Create QC Workspace

```bash
mkdir genome_lab
cd genome_lab

mkdir good_sequence bad_sequence
```

### Create FASTA Files

```bash
cd good_sequence

touch sample1.fasta sample2.fasta sample3.fasta
```

### Add Sequence Data

```bash
echo ">Human_1" > sample1.fasta
echo "ATGCGTACCGTAGGCTA" >> sample1.fasta

echo ">Human_2" > sample2.fasta
echo "ATGCGNNNNNTAGCTA" >> sample2.fasta

echo ">Human_3" > sample3.fasta
echo "ATGGTTAACCGGTTA" >> sample3.fasta
```

### Create Corrupted Files

```bash
cd ../bad_sequence

touch corrupted1.fasta corrupted2.fasta
```

---

## 🔍 FASTA Quality Control

### Find Empty FASTA Files

```bash
find . -type f -empty
```

Output:

```text
./bad_sequence/corrupted1.fasta
./bad_sequence/corrupted2.fasta
./reports/corrupted.fasta
```

---

### Search for Ambiguous Bases (N)

```bash
grep -R "N"
```

Output:

```text
good_sequence/sample2.fasta:ATGCGNNNNNTAGCTA
```

---

### Count Files Containing Ambiguous Bases

```bash
grep -R "N" | wc -l
```

Output:

```text
1
```

---

## 📊 QC Report Generation

### Create Summary Report

```bash
cd reports

touch day11_summary.txt

echo "Total empty FASTA files: 3" > day11_summary.txt
echo "Files containing N: 1" >> day11_summary.txt
```

### Verify Report

```bash
cat day11_summary.txt
```

Output:

```text
Total empty FASTA files: 3
Files containing N: 1
```

---

## 🚑 Quarantine Workflow

Move corrupted files to quarantine:

```bash
mkdir quarantine

mv bad_sequence/corrupted1.fasta \
bad_sequence/corrupted2.fasta \
quarantine
```

Verify:

```bash
cd quarantine
ls
```

Output:

```text
corrupted1.fasta
corrupted2.fasta
```

---

## ⚠️ Debugging Journey

### Mistake 1

```bash
cat -l day11_summary.txt
```

Output:

```text
cat: invalid option -- 'l'
```

Fix:

```bash
ls -l day11_summary.txt
```

---

### Mistake 2

```bash
cd..
```

Output:

```text
command not found
```

Fix:

```bash
cd ..
```

---

### Mistake 3

```bash
find . -type f -name "(*.fasta)" | wc -l
```

Output:

```text
0
```

Fix:

```bash
find . -type f -name "*.fasta" | wc -l
```

Output:

```text
16
```

---

### Mistake 4

```bash
mv bad_sequence/corrupted1.fasta quarantine
```

Output:

```text
No such file or directory
```

Fix:

```bash
mkdir quarantine
mv bad_sequence/corrupted1.fasta quarantine
```

---

## 🔬 Bioinformatics Relevance

Quality control is one of the first steps in every bioinformatics pipeline.

Before performing:

- Genome Assembly
- Variant Calling
- RNA-Seq Analysis
- Sequence Alignment

researchers must identify:

- Corrupted files
- Empty files
- Ambiguous nucleotides (`N`)
- Improper FASTA formatting

This project simulates those initial QC checks using Linux tools.

---

## 📈 Workflow

```text
Create FASTA Files
          ↓
Generate Corrupted Files
          ↓
Detect Empty Files
          ↓
Search Ambiguous Bases (N)
          ↓
Generate QC Report
          ↓
Quarantine Problematic Files
          ↓
Prepare Dataset For Analysis
```

---

## 🚀 Future Improvements

- Automate QC using Bash scripts
- Calculate GC content from terminal
- Validate FASTA headers automatically
- Generate CSV QC reports
- Integrate QC pipeline with Python
- Process real genomic datasets

---

## 🎯 Goal

Develop Linux-based quality-control workflows for biological sequence datasets and build a strong foundation for real-world bioinformatics data processing. 🧬🐧
