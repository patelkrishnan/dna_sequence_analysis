# DNA Sequence Analysis Tool

This tool provides a set of functionalities to analyze and manipulate DNA sequences. It can validate the input sequence, calculate the GC content, determine the nucleotide frequencies, and generate the complement, reverse, and reverse complement sequences.

## Features

- **Validation of DNA Sequence**: Validates the input DNA sequence to ensure it contains only valid nucleotides (A, T, C, G).
  
- **Calculation of GC Content**: Calculates the GC content of the input DNA sequence.
  
- **Calculation of Nucleotide Frequencies**: Determines the frequencies of each nucleotide (A, T, C, G) in the input DNA sequence and plots them.
  
- **Generation of Complement Sequence**: Generates the complement sequence of the input DNA sequence.
  
- **Generation of Reverse Sequence**: Generates the reverse sequence of the input DNA sequence.
  
- **Generation of Reverse Complement Sequence**: Generates the reverse complement sequence of the input DNA sequence.

## Requirements

- Python 3.x
- Matplotlib

## Usage

To run the DNA Sequence Analysis Tool, use the following command:

```bash
python dna_sequence_analysis.py [input_sequence]
```
### Example usage ###

`python dna_sequence_analysis.py ATCGATCG`

### Example output
```
Sequence Length: 8
GC Content: 0.5
Nucleotide Frequencies: {'A': 2, 'T': 2, 'C': 2, 'G': 2}

[Bar plot showing the nucleotide frequencies]

Complement Sequence: TAGCTAGC
Reverse Sequence: GCTAGCTA
Reverse Complement Sequence: CGATCGAT
```

## Author
Krishna Patel
