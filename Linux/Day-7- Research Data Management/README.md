# Day 7 - Research Data Management 🐧🧬

## Environment
- OS: Windows 11 + WSL2 (Ubuntu)
- Linux user: `ankan_bioinfo`
- Workspace: `/home/ankan_bioinfo/research_data`

---

## 🎯 Objective
Build a complete mock bioinformatics research project
structure from scratch using only Linux terminal commands.

---

## 📁 Project Structure
```text
research_data/
│
├── human/
│   ├── sample1.fasta   →  >Human_Sample1    | ATGCGTACCGTAGGCTA
│   └── sample2.fasta   →  >Human_Sample2    | GGCTTATGAAACCGTTA
│
├── bacteria/
│   ├── ecoli.fasta     →  >Ecoli_K12        | ATGGGTTAACCGGGTAA
│   └── salmonella.fasta → >Salmonella_Typhi | TATAGGGCCCATGTTAA
│
├── backup/
│   ├── sample1.fasta
│   ├── sample2.fasta
│   ├── ecoli.fasta
│   └── salmonella.fasta
│
└── reports/
    └── corrupted.fasta  ← empty file detected
```

---

## 🖥️ Linux Commands Practiced

```bash
# Directory creation
mkdir research_data
cd research_data
mkdir human bacteria backup reports

# FASTA file creation
touch sample1.fasta sample2.fasta
touch ecoli.fasta salmonella.fasta

# Writing FASTA format sequences
echo ">Human_Sample1" > sample1.fasta
echo "ATGCGTACCGTAGGCTA" >> sample1.fasta

echo ">Ecoli_K12" > ecoli.fasta
echo "ATGGGTTAACCGGGTAA" >> ecoli.fasta

# Backing up all FASTA files
cp human/sample1.fasta human/sample2.fasta \
   bacteria/ecoli.fasta bacteria/salmonella.fasta \
   backup/

# Find all FASTA files
find . -type f -name "*.fasta"

# Search for ATG start codon
grep -R "ATG"

# Search for FASTA headers
grep -R "^>"

# Find empty files
find . -type f -empty

# Recursive directory listing
ls -R
```

---

## ⚠️ Mistakes & Debugging

### Typo errors
```bash
cd reserach_data     ❌  # misspelled
cd research_data     ✅
```

### Directory vs file confusion
```bash
cat human            ❌
# Error: cat: human: Is a directory
cd human             ✅
```

### Copy command mistakes
```bash
# Used output redirection instead of destination
cp sample1.fasta sample2.fasta > backup    ❌
# > is redirection, not a folder destination!

# Fix — must be at correct parent directory:
cp human/sample1.fasta human/sample2.fasta \
   bacteria/ecoli.fasta bacteria/salmonella.fasta \
   backup/             ✅
```

### Accidentally created empty backup files
```bash
# human/backup and bacteria/backup created as empty files
# Detected using:
find . -type f -empty

# Output:
./human/backup
./bacteria/backup
./reports/corrupted.fasta
```

---

## 🔬 Bioinformatics Connection

| Linux Command | Bioinformatics Use |
|--------------|-------------------|
| `echo ">" > file` | Create FASTA header |
| `echo "seq" >> file` | Append DNA sequence |
| `grep -R "^>"` | Count sequences in project |
| `grep -R "ATG"` | Find start codons across files |
| `find -name "*.fasta"` | Locate all sequence files |
| `find -empty` | Detect corrupted/empty files |
| `cp` | Backup genome files before analysis |
| `ls -R` | Inspect full project structure |

---

## 💡 Key Takeaway
Today I built a real bioinformatics research directory
structure with human and bacterial FASTA files — exactly
how research labs organize genomic data before analysis.

The backup workflow mirrors real bioinformatics pipelines
where raw data is always backed up before processing. 🔬

---

## 🌱 Learning Resources
- 📺 [Linux Command Line Tutorial For Beginners | ProgrammingKnowledge](https://youtube.com/playlist?list=PLS1QulWo1RIb9WVQGJ_vh-RQusbZgO_As)

---

## 🎯 Goal
Master Linux file management for organizing and
processing real biological sequence data. 🧬
