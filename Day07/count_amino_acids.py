# count_amino_acids.py

import sys
from collections import Counter

# Codon to amino acid mapping
codon_table = {
    'Phe': ['TTT', 'TTC'],
    'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile': ['ATT', 'ATC', 'ATA'],
    'Met': ['ATG'],
    'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr': ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr': ['TAT', 'TAC'],
    'His': ['CAT', 'CAC'],
    'Gln': ['CAA', 'CAG'],
    'Asn': ['AAT', 'AAC'],
    'Lys': ['AAA', 'AAG'],
    'Asp': ['GAT', 'GAC'],
    'Glu': ['GAA', 'GAG'],
    'Cys': ['TGT', 'TGC'],
    'Trp': ['TGG'],
    'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP': ['TAA', 'TAG', 'TGA']
}

# Reverse lookup: codon -> amino acid
codon_to_aa = {codon: aa for aa, codons in codon_table.items() for codon in codons}


def read_sequence_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Remove FASTA headers (lines starting with >)
    sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return sequence.upper()


def count_amino_acids(sequence):
    amino_acid_counter = Counter()

    for i in range(0, len(sequence) - 2, 3):  # Step by 3
        codon = sequence[i:i + 3]
        if len(codon) == 3:
            amino_acid = codon_to_aa.get(codon, None)
            if amino_acid:
                amino_acid_counter[amino_acid] += 1

    return amino_acid_counter


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_amino_acids.py <sequence_file>")
        sys.exit(1)

    filename = sys.argv[1]
    dna_sequence = read_sequence_from_file(filename)
    aa_counts = count_amino_acids(dna_sequence)

    print("\nAmino Acid Counts:")
    for aa, count in aa_counts.items():
        print(f"{aa}: {count}")