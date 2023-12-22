"""
File: find_complementary_dna_strand.py
Prints the complementary strand of a provided DNA string
"""

import argparse


def main():
    """ Business Logic """
    args = get_cli_args()
    dna_filename = args.input
    dna_string = get_dna_string(dna_filename)
    reverse_complement_string = get_dna_reverse_complement(dna_string)
    print(reverse_complement_string)


def get_dna_string(dna_filename):
    """
    obtains the dna string from the file
    :param dna_filename: name of file containing dna sequence
    :return: a string of the DNA sequence
    """

    dna_string = ""
    with open(dna_filename, "r", encoding='utf-8') as fh_in:
        for line in fh_in:
            dna_string += line.strip()
    return dna_string


def get_dna_reverse_complement(dna):
    """
    obtains the reverse complementary strand
    :param dna: dna string
    :return: reverse complement of dna string
    """
    reverse_string = dna[::-1]
    # A and T conversion
    reverse_complementary_string = (reverse_string.replace('A', 'Z')
                                    .replace('T', 'A').replace('Z', 'T'))

    # G and C conversion
    reverse_complementary_string = (reverse_complementary_string.replace('G', 'Z')
                                    .replace('C', 'G').replace('Z', 'C'))

    return reverse_complementary_string


def get_cli_args():
    """
    CLI options using Python's argparse
    @return: Instance of argparse arguments
    """

    parser = argparse.ArgumentParser(description='provide the name of the dna file')

    parser.add_argument('-i', '--input', default='testfile.txt',
                        type=str, help='takes input file name',
                        required=False)

    return parser.parse_args()


if __name__ == "__main__":
    main()
