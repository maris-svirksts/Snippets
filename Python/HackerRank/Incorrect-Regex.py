#! python

# https://www.hackerrank.com/challenges/incorrect-regex/problem

import re

element_count = int(input())

for i in range(element_count):
    input_to_check = input()
    try:
        x = re.search(input_to_check, "")
        print('True')
    except Exception:
        print('False')