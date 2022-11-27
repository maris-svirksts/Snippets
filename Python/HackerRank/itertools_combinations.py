# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

letters, comb = input().split(' ', 2)
letters, comb = sorted(letters), int(comb)

for i in range(1, comb + 1):
    [print(''.join(x)) for x in list(combinations(letters, i))]