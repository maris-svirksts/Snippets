#!python

# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

input_counter = int(input())

for _ in range(input_counter):
    phone = input()
    if re.search(r"^[789][0-9]{9}$", phone):
        print('YES')
    else:
        print('NO')