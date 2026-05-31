# Day 4 - Dictionary, Sets & Loops 🐍🧬

## Topics Learned

### 📚 Dictionary
- Key-value pairs, mutable & unordered
- Nested Dictionaries
- Dictionary Methods (`keys`, `values`, `items`, `get`, `update`)

### 📚 Sets
- Unordered, unique elements
- Set Methods (`add`, `remove`, `clear`, `pop`, `union`, `intersection`)

### 📚 Loops
- `while` loop
- `for` loop & `for` with `else`
- `range()` — start, stop, step
- `break`, `continue`, `pass` statements

---

## Bioinformatics Connection 🔬

| Python Concept | Bioinformatics Use |
|----------------|-------------------|
| `dict` | Store gene name → function mapping |
| `dict.get()` | Safely retrieve gene annotations |
| `set` | Store unique gene IDs, remove duplicates |
| `while` loop | Traverse DNA sequences base by base |
| `for` loop | Iterate over gene lists |
| `break` | Stop search when target gene is found |

---

## Practice Problems

### 🧬 Bioinformatics Problems
1. Gene Database — store cancer genes with functions using dictionary
2. GC Content Calculator — using while loop
3. DNA Nucleotide Counter — using while loop
4. DNA Complement Generator — using while loop *(improved from Day 3!)* 🔥

### 🐍 Python Problems
5. Word Meaning Dictionary
6. Subject Marks Dictionary
7. Subjects Set (unique classroom counter)
8. Store 9 & 9.0 as separate values in dictionary
9. Print 1 to 100 using while & for
10. Print 100 to 1
11. Multiplication table of 5 (while)
12. Multiplication table of n (while & for)
13. Squares of 1 to 10
14. Sum of first n numbers (while)
15. Factorial of n (for)
16. Print list elements using for
17. Search number in tuple using while & for

---

## Example — Gene Database
```python
gene = {
    "TP53": "Tumor Suppressor",
    "BRCA1": "DNA Repair",
    "EGFR": "Growth Receptor"
}
gene.update({"MYC": "Cell Growth Regulation"})
print(gene.get("TP53"))  # Output: Tumor Suppressor
```

---

## What This Means Biologically 🔬
Dictionaries are the backbone of bioinformatics databases:
- Gene annotation databases map gene IDs to functions
- Protein databases map sequence IDs to structures
- Sets remove duplicate sequencing reads before analysis
- Loops traverse every base in a DNA sequence — essential
  for GC content, complement generation, and motif finding

---

## Key Takeaway 💡

Today I learned how to organize biological information using dictionaries and sets, and how to automate repetitive tasks using loops.

By combining loops with DNA sequence analysis, I took another step toward building real bioinformatics workflows instead of solving only generic programming problems.
## Future Improvements 🚀
- Parse and analyze FASTA-formatted DNA sequences
- Build a gene lookup tool using dictionary
- Apply `set.intersection()` to find common genes
  between two datasets

---

## Learning Resources
- 📺 [Lecture 4 : Dictionary & Set in Python | Apna College](https://youtu.be/078tYSD7K8E?si=fRErVGaNBbSlZOU6)
- 📺 [Lecture 5 : Loops in Python | While & For Loops | Apna College](https://youtu.be/S73thl0AyFU?si=Bv3dlQFD3uSXp7Bn)
- 🌐 [FreeCodeCamp Python](https://www.freecodecamp.org/learn/python-v9/)

---

## Notes
- [Lecture4_py.pdf](https://drive.google.com/file/d/1FE_OCfJOb-fd3qVrpKS2iIwTxVj4NENa/view?usp=drive_link)
- [Lecture5_py.pdf](https://drive.google.com/file/d/1qIpsTq_pcBoJjpNMk4hAG-sKvXJQ4MV1/view?usp=drive_link)

---

## Goal
Use Python data structures and loops to process
biological data — iterating over sequences, building
gene databases, and finding unique genomic elements. 🧬
