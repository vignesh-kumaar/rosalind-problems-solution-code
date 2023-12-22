"""
file : nucleotide-count-in-dna-string.py
counts (in case-sensitive) the number of each nucleotide in a DNA string file
"""


def main():
    # open the txt file containing the dna sequence
    fh_in = open("rosalind_dna.txt", "r")

    # store the information from the file in a string
    data = ""
    for line in fh_in:
        data += line.strip()

    # close the file
    fh_in.close()

    # declare initial dictionary with 0 counts of each nucleotide
    nucleotide_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    # counts the number of each nucleotide in the string
    for character in data:
        if character in ('A', 'G', 'C', 'T'):
            nucleotide_count[character] += 1

    # prints the output
    print(f"{nucleotide_count['A']} {nucleotide_count['C']} "
          f"{nucleotide_count['G']} {nucleotide_count['T']}")


if __name__ == "__main__":
    main()
