import itertools
from itertools import product
import string


norohind = "^/^d^n^i^h^o^r^o^n"


def repeats(n: int):
    # for i in range(1, n + 1):
    #     for char in string.ascii_letters:
    #         print(f'{norohind}{("$" + char)*i}')
    for comb in itertools.permutations(string.ascii_letters, r=3):
        a = '$' + '$'.join(comb)
        print(f'{norohind}{a}')


repeats(10)
