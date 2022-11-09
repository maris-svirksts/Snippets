# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

name, size = input().split()

result = [''.join(i) for i in list(permutations(name, int(size)))]
result.sort()

[print(y) for y in result]