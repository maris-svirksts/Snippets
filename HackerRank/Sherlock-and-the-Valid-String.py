#!python

# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    elements = {}

    for character in s:
        elements[character] = elements.get(character, 0) + 1

    unique_counts = Counter(elements.values())

    if len(unique_counts) == 1:
        return "YES"
    elif (len(unique_counts) == 2):
        if 1 in unique_counts.keys() and unique_counts[1] == 1:
            return "YES"
        elif max(unique_counts.keys()) - min(unique_counts.keys()) == 1 and 1 in unique_counts.values():
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

if __name__ == '__main__':
    s = input()

    print(isValid(s))
