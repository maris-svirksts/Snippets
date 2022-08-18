# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import email.utils
import re

input_counter = int(input())

for _ in range(input_counter):
    email_to_validate = input()
    parsed_version = email.utils.parseaddr(email_to_validate)

    if re.search(r"^[a-zA-Z][A-Za-z0-9-,\.,_]*\@[a-zA-Z]*\.[a-zA-Z]{1,3}$", parsed_version[1]):
        print(email_to_validate)