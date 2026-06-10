# 🧬 Day 9 — My First Bioinformatics OOP Class

## 🎯 Objective

After spending several days building bioinformatics tools using functions, I wanted to learn how real software organizes code.

Today's goal was to take my first step into **Object-Oriented Programming (OOP)** and apply it directly to bioinformatics instead of using generic examples.

---

# 🚀 Where I Started

Before today, I had already built:

* FASTA Reader
* GC Content Calculator
* Reverse Complement Generator
* Nucleotide Counter
* Motif Finder
* Mutation Detector

All of these tools were written using functions.

Although they worked correctly, I wanted to understand how these tools could be organized more effectively.

---

# 📚 OOP Concepts Learned

From today's lecture, I learned:

### Class

A blueprint used to create objects.

### Object

An instance of a class.

### Constructor

```python
__init__()
```

Used to initialize object attributes.

### Attributes

Variables belonging to an object.

### Methods

Functions belonging to an object.

### self

A reference to the current object.

### Static Methods

Methods that work at the class level.

### Abstraction

Showing only essential functionality while hiding implementation details.

### Encapsulation

Combining data and functions into a single unit.

---

# 🧬 First Bioinformatics OOP Project

Instead of creating traditional beginner examples like:

```python
class Student:
```

or

```python
class Car:
```

I decided to build a biologically relevant class.

```python
class DNASequence:
```

---

# 🔬 DNASequence Class

The idea was simple:

A DNA sequence should be treated as an object.

Example:

```python
human = DNASequence("ATGCGTAC")
```

The object should be capable of performing biological analyses on itself.

---

# ⚙️ Features Implemented

## ✅ Sequence Storage

Stores a DNA sequence as an object attribute.

Example:

```python
human = DNASequence("ATGCGTAC")
```

---

## ✅ Sequence Display

Displays the stored sequence.

Example Output:

```text
DNA Sequence: ATGCGTAC
```

---

## ✅ Sequence Length Calculation

Returns:

```text
8
```

---

## ✅ GC Content Analysis

For:

```text
ATGCGTAC
```

Output:

```text
50.0%
```

---

## ✅ Reverse Complement Generation

For:

```text
ATGCGTAC
```

Output:

```text
GTACGCAT
```

---

# 🔄 From Functions to Methods

One of the biggest lessons today was understanding how previously written functions can become class methods.

Earlier:

```python
def gc_content(sequence):
```

Now:

```python
def gc_content(self):
```

Similarly:

```python
def reverse_complement(sequence):
```

became:

```python
def reverse_complement(self):
```

The logic remained the same, but the organization became much cleaner.

---

# ⚠️ Debugging Journey

While building the class, I encountered several issues.

### Constructor Mistakes

Initially I made errors while defining attributes inside:

```python
__init__()
```

---

### Missing Assignment Operator

Example:

```python
self.length len(sequence)
```

instead of:

```python
self.length = len(sequence)
```

---

### Reverse Complement Errors

Forgot to initialize:

```python
complement = ""
```

before building the complementary strand.

---

### Loop Errors

Forgot:

```python
i += 1
```

inside a loop.

---

### Understanding self

One of the most important concepts I struggled with initially was:

```python
self
```

By the end of the project, I understood that it refers to the current object and allows methods to access object data.

---

# 🧠 Biggest Realization

The most valuable lesson from today was:

> OOP does not replace previous knowledge. It organizes it.

The GC content calculator, reverse complement generator, and sequence-analysis logic stayed exactly the same.

The difference was learning how to package them inside an object.

---

# 📈 Skills Strengthened

## Python

✅ Functions

✅ Loops

✅ Conditionals

✅ Dictionaries

---

## OOP

✅ Classes

✅ Objects

✅ Constructors

✅ Attributes

✅ Methods

✅ self

✅ Encapsulation

✅ Abstraction

---

## Bioinformatics

✅ DNA Sequence Analysis

✅ GC Content

✅ Reverse Complements

✅ Sequence Statistics

✅ Bioinformatics Tool Design

---

# 🎯 What I Still Need Practice On

* Writing classes from memory
* Designing larger classes
* Using constructors confidently
* Distinguishing attributes from methods
* Building multi-object projects

---

# 🚀 Next Steps

* Practice Student and Account classes
* Build an ORF Finder
* Convert more bioinformatics tools into classes
* Strengthen OOP fundamentals
* Continue building project-based bioinformatics tools

---

# 🏆 Day 9 Outcome

Today marked my transition from procedural programming to object-oriented programming.

For the first time, I successfully designed a biologically relevant class and began understanding how real bioinformatics software can be structured.

**Status:** 🚀 First Bioinformatics OOP Class Completed Successfully 🧬🐍💻
