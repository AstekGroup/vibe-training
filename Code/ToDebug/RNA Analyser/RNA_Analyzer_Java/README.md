# RNA Association Analyzer

This Java program analyzes the `bdd_asso_extrait.csv` file to count associations per department and identify associations with empty 'objet' fields.

## Features:

- Counts associations based on the first two digits of the postal code (department).
- Counts associations where the 'objet' field is empty.
- Provides a progress indicator for large files.
- Optimized for performance using `BufferedReader` and efficient string parsing.

## File Location:

The `bdd_asso_extrait.csv` file is expected to be in the parent directory: `/Users/philippe.pary/Documents/Formations/Vibe coding/Code/ToDebug/RNA Analyser/`

## How to Compile:

Navigate to the `RNA_Analyzer_Java` directory and compile the Java source file:

```bash
javac RNAAnalyzer.java
```

## How to Run:

After successful compilation, run the program from the `RNA_Analyzer_Java` directory:

```bash
java -cp . RNAAnalyzer
```

## Output:

The program will print the total number of lines processed, a progress update during execution, the number of associations per department, and the total count of associations with an empty 'objet' field.
