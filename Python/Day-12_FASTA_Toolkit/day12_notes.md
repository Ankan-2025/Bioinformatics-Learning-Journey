# Day 12 - Mini Bioinformatics Toolkit + Git/GitHub/SSH 🐍🧬🐙

## 📌 Overview
Day 12 combined everything learned so far into one complete
toolkit, and introduced real version control — Git, GitHub,
and SSH authentication — replacing manual browser uploads.

---

## 🧬 Mini Bioinformatics Toolkit

A single script that performs full DNA sequence analysis
on FASTA files.

### Features
| Function | Purpose |
|----------|---------|
| read_fasta() | Parses FASTA file into header-sequence dictionary |
| gc_counter() | Calculates GC content % |
| rebuild_reverse_complement() | Generates reverse complement strand |
| nucleotide_counter() | Counts & calculates % of A, T, G, C |
| mutation_detector() | Compares sequences against a reference |
| orf_finder() | Detects multiple ORFs, reports if none found |
| report_generator() | Summarizes total sequences, longest sequence, total bp |

### Sample Output
text
Header: >Human
GC content: 50.0 %
Reverse complement: GTACGCAT
Length of nucleotide: 8
A: 2  25.0%
T: 2  25.0%
G: 2  25.0%
C: 2  25.0%

Analyzing: >Human
ORF 1: ATGCGTAC
Length of ORF: 8

Reference sequence (#Seq 1): ATGCGTAC
Comparing sequence #2: ATGAGTTC
Mutation found at position 4: C → A
Mutation found at position 7: A → T
Total mutations found in sequence #2: 2

Total Sequences: 3
>Human Length: 8
>Mouse Length: 8
>Virus Length: 8
Longest Sequence: >Human
Total Nucleotides: 24


---

## 🐙 Git & GitHub Workflow

Moved from browser file uploads to proper command-line
version control.

### Commands Practiced
bash
git clone
git status
git add .
git commit -m "Day 12: FASTA parser, ORF finder, mutation detector and statistics report"
git push
git remote -v
git remote set-url origin
git config --global user.name
git config --global user.email


### SSH Authentication Setup
bash
ssh-keygen
ssh-add

Configured SSH keys to authenticate with GitHub instead
of repeated password prompts — the standard approach used
in professional development workflows.

---

## 🐧 Linux Commands Used
bash
ls    cd    mkdir   touch
nano  cat   python3


---

## ⚠️ Problems Solved

| Error | Cause | Fix |
|-------|-------|-----|
| FileNotFoundError | Wrong FASTA filename/path | Corrected file path |
| NameError | Typo in variable name | Fixed variable reference |
| TypeError | Wrong arguments passed to function | Corrected function call |
| GitHub auth failure | HTTPS password auth deprecated | Set up SSH key authentication |

---

## 🔬 Bioinformatics Connection

| Tool Feature | Real-World Use |
|-------------|----------------|
| FASTA Parser | Reading genome/sequencing data |
| GC Content | DNA stability, primer design |
| Reverse Complement | Strand analysis, primer design |
| ORF Finder | Gene prediction |
| Mutation Detector | Variant calling, comparative genomics |
| Report Generator | Dataset summary before analysis |

---

## 🎯 Key Outcomes
- Combined 5 days of bioinformatics functions into one toolkit ✅
- Moved from manual uploads to Git/GitHub version control ✅
- Set up SSH authentication for GitHub ✅
- Debugged 3 different error types independently ✅

---

## 🚀 Next Goals
- Round percentage outputs to 2 decimal places
- Extend report_generator to include GC% and ORF summary
- Convert toolkit into a proper Python package
- Start exploring Biopython
- Use git branches for new features

---

## 🏆 Day 12 Outcome
Built a complete Mini Bioinformatics Toolkit and learned
the real-world workflow of managing code with Git, GitHub,
and SSH authentication — moving from a beginner uploading
files to a developer managing version-controlled projects. 🧬🐙
