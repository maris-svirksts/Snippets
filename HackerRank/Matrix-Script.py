#!/bin/python3

# https://www.hackerrank.com/challenges/matrix-script/problem

import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

rotated_list = list(zip(*matrix))
merged_list  = ''.join(str(item) for innerlist in rotated_list for item in innerlist)
result       = re.sub(r"[^\d\w]+(?=[\d\w])", " ", merged_list)
print(result)
