#! python

# https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re

counter = int(input())

for _ in range(counter):
    variable = input()

    if re.search("^\d+$", variable):
        print("False")
    else:
        try:
            float(variable)
            print("True")
        except Exception:
            print("False")