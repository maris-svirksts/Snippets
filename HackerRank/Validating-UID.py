# https://www.hackerrank.com/challenges/validating-uid/problem

import re

input_count = int(input())

for _ in range(input_count):
    current_uid = input()
    if len(set(current_uid)) is not len(current_uid):
        print("Invalid")
    elif not re.search(r"^[a-zA-Z0-9]{10}$", current_uid):
        print("Invalid")
    elif not re.search(r"([^A-Z]*[A-Z]){2,}", current_uid):
        print("Invalid")
    elif not re.search(r"([^\d]*\d){3,}", current_uid):
        print("Invalid")
    else:
        print("Valid")