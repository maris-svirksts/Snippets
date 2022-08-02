#! python

# https://www.hackerrank.com/challenges/validating-credit-card-number/problem

import re

line_count = int(input())
word_list = {}

for i in range(line_count):
    credit_card = input().strip()
    result = re.search(r"^[456][0-9]{3}[-]{0,1}[0-9]{4}[-]{0,1}[0-9]{4}[-]{0,1}[0-9]{4}$", credit_card)

    if result:
        credit_card = credit_card.replace('-', '')
        if re.search(r"(\d)\1{3,}", credit_card):
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")