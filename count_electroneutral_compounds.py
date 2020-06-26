#! /usr/bin/env python3
from itertools import combinations_with_replacement
from typing import Sequence

n_ions = 5
data_file = "157numb"


#def all_electroneutral_combinations(charges: Sequence, n_ions: int) -> list:
def all_electroneutral_combinations(charges: Sequence[int], n_ions: int) -> list:
    """Given a list of charges, return all the neutral combinations

    Combinations include repetition (i.e. for charges=[-1, 2], n_ions=3
    [-1, -2, 2] would be found as a neutral combination)

    Args:
        charges: Sequence of charges to consider
        n_ions: number of charges to combine in each considered combination

    Returns:
        List of neutral combinations from input charges
    """

    return [x for x in combinations_with_replacement(charges, n_ions)
            if sum(x) == 0]


with open(data_file, 'rt') as fd:
    charges_from_file = [int(line.rstrip('\n')) for line in fd]

print("Neutral combinations: {}".format(
    len(all_electroneutral_combinations(charges_from_file, n_ions))))
