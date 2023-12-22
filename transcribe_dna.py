"""
File: transcribe-dna.py
Transcribes a dna data file and outputs the corresponding rna
"""

import argparse


def main():
    """ Business Logic """
    args = get_cli_args()
    dna_filename = args.input
    dna_string = get_dna_string(dna_filename)
    rna_string = dna_string.replace('T', 'U')
    print(rna_string)


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
