"""
File: find_rabbit_population.py
Finds the rabbit-pair population provided two variables n and k using a modified fibonacci sequence
"""

import argparse
import sys
from functools import lru_cache


def main():
    """ Business Logic """
    # obtain filename information from user
    args = get_cli_args()
    filename = args.input

    # extract n and k from the provided file
    n, k = get_n_and_k(filename)

    # print output of function call that calculates the population pair size
    print(f"{get_population_pair_size(int(n), int(k))}")


def get_n_and_k(filename):
    """
    obtains the n and k information from the file
    :param filename: name of file to open
    :return: strings with n and k
    """

    with open(filename, "r") as fh_in:
        for line in fh_in:
            values = line.strip().split()
    # values[0] contains the value of n and values[1] contains the value of k
    return values[0], values[1]


@lru_cache(maxsize=1000)
def get_population_pair_size(n, k):
    """
    obtains the population pair size for the provided parameters
    :param n: nth term of sequence
    :param k: each reproduction age rabbit produces k pairs of offspring
    :return: integer containing the population pair size
    """

    # sequence starts with n = 1
    if n < 1:
        sys.exit("incorrect value of n")

    # the first two terms of the fibonacci sequence are defined to be 1
    if n == 1 or n == 2:
        return 1

    # fibonacci sequence but with k multiplied to the n-2th term
    # this accounts for the number of offspring that each reproduction age rabbit
    # produces
    return get_population_pair_size(n-1, k) + k * get_population_pair_size(n-2, k)


def get_cli_args():
    """
    CLI options using Python's argparse
    @return: Instance of argparse arguments
    """

    parser = argparse.ArgumentParser(description='provide a file with the variables n and k'
                                                 'separated by a space')

    parser.add_argument('-i', '--input', default="testfile.txt",
                        type=str, help='takes input file',
                        required=False)

    return parser.parse_args()


if __name__ == "__main__":
    main()