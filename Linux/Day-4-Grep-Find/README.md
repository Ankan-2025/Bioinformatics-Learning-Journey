# Day 5 - Linux grep, find & Bioinformatics Lab Setup 🐧🧬

## Environment
- OS: Windows 11 + WSL2 (Ubuntu)
- Linux user: `ankan_bioinfo`
- Workspace: `/home/ankan_bioinfo/bio_lab`

---

## Commands Learned

| Command | What it does |
|---------|-------------|
| `grep` | Search for patterns inside files |
| `grep -c` | Count matching lines |
| `grep -o` | Extract only matching text |
| `grep -R` | Search recursively through directories |
| `wc -l` | Count lines of output |
| `find` | Search for files and directories |
| `find -empty` | Find empty files |
| `find -delete` | Delete found files |
| `cd -` | Go back to previous directory |

---

## Practice Done — Bioinformatics Lab Setup
```bash
# Created a structured bioinformatics lab
mkdir bio_lab
cd bio_lab
mkdir dna_samples reports trash

# Created DNA sample files
cd dna_samples
touch sample1.txt sample2.txt sample3.txt

# Stored DNA sequences
echo ATGCGTACCGTA > sample1.txt
echo GGGTTTCCCAA > sample2.txt
echo ATGAAATTTGGG > sample3.txt

# Searched for ATG start codon across ALL samples
grep ATG *.txt

# Counted G occurrences in sample1
grep -o "G" sample1.txt | wc -l

# Recursive search for ATG across entire lab
grep -R "ATG" 

# Found and deleted empty files
find -empty
find -delete
```

---

## Errors & Fixes 🔧
```bash
$ grep -o "G" sample1.txt | wx -1
# Error: wx command not found
# Fix: wc (not wx)

$ grep -o "G" sample1.txt | wc -1
# Error: invalid option -1
# Fix: wc -l (letter l, not number 1)

$ cd..
# Error: command not found
# Fix: cd .. (space required)

$ cd-
# Error: command not found
# Fix: cd - (space required)
```

---

## Bioinformatics Connection 🔬

| Linux Command | Bioinformatics Use |
|--------------|-------------------|
| `grep ATG *.txt` | Search for start codons across sample files |
| `grep -o "G" \| wc -l` | Count specific nucleotide occurrences |
| `grep -R "ATG"` | Search entire project for sequence motifs |
| `find -empty` | Detect empty sequence files before analysis |
| `find -delete` | Clean up temporary analysis files |

---

## Key Takeaway 💡
Today I built a real bioinformatics lab structure in Linux
and used `grep` to search for biological patterns across
multiple DNA sequence files — simulating how researchers
search for sequence motifs in genomic datasets.

The command `grep ATG *.txt` is essentially what
bioinformatics tools do when scanning genomes for
translation start sites. 🔬

---

## Learning Resources
- 📺 [Mastering Linux GREP Command with 15+ Practical Use Cases](https://youtu.be/bKNAYemzC6E?si=YzOsYFfR5JUovU1B)
- 📺 [Linux FIND COMMAND Tutorial With Practical 12 Use Cases](https://youtu.be/1z17BswGsdw?si=khS66RnQ6sBn6x2o)
- 📺 [Linux Command Line Tutorial For Beginners | ProgrammingKnowledge](https://youtube.com/playlist?list=PLS1QulWo1RIb9WVQGJ_vh-RQusbZgO_As)

---

## Goal
Use Linux command line tools to search, filter, and manage
biological sequence files — building toward real
bioinformatics pipeline automation. 🧬
