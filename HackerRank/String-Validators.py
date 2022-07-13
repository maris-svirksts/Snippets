#! python

# https://www.hackerrank.com/challenges/string-validators/problem
import re

if __name__ == '__main__':
    s = input()

    print("True") if re.search("[a-zA-Z0-9]+", s) else print("False")
    print("True") if re.search("[a-zA-Z]+", s) else print("False")
    print("True") if re.search("[0-9]+", s) else print("False")
    print("True") if re.search("[a-z]+", s) else print("False")
    print("True") if re.search("[A-Z]+", s) else print("False")
    