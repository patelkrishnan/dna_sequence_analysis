import argparse
import matplotlib.pyplot as plt
import numpy as np

# Function to validate DNA sequence
def is_valid_sequence(sequence):
    valid_bases = set('ATCG')
    return all(base in valid_bases for base in sequence)

# Function to calculate GC content
def calculate_gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    return gc_count / len(sequence)

# Function to calculate nucleotide frequencies
def calculate_nucleotide_frequencies(sequence):
    nucleotide_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for base in sequence:
        if base in nucleotide_counts:
            nucleotide_counts[base] += 1
    return nucleotide_counts

# Function to plot nucleotide frequencies
def plot_nucleotide_frequencies(nucleotide_counts):
    bases = list(nucleotide_counts.keys())
    counts = list(nucleotide_counts.values())
    plt.bar(bases, counts)
    plt.xlabel('Nucleotide')
    plt.ylabel('Count')
    plt.title('Nucleotide Frequencies')
    plt.show()

# Function to complement DNA sequence
def complement_sequence(sequence):
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement_map[base] for base in sequence)

# Function to reverse DNA sequence
def reverse_sequence(sequence):
    return sequence[::-1]

# Function to reverse complement DNA sequence
def reverse_complement_sequence(sequence):
    return reverse_sequence(complement_sequence(sequence))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DNA Sequence Analysis Tool")
    parser.add_argument("sequence", help="Input DNA sequence")
    args = parser.parse_args()

    sequence = args.sequence.upper()

    # Validate sequence
    if not is_valid_sequence(sequence):
        print("Invalid DNA sequence. Please input a sequence containing only A, T, C, and G nucleotides.")
        exit()

    print("Sequence Length:", len(sequence))
    print("GC Content:", calculate_gc_content(sequence))

    # Calculate nucleotide frequencies
    nucleotide_counts = calculate_nucleotide_frequencies(sequence)
    print("Nucleotide Frequencies:", nucleotide_counts)

    # Plot nucleotide frequencies
    plot_nucleotide_frequencies(nucleotide_counts)

    print("Complement Sequence:", complement_sequence(sequence))
    print("Reverse Sequence:", reverse_sequence(sequence))
    print("Reverse Complement Sequence:", reverse_complement_sequence(sequence))