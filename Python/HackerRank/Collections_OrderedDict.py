# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

ordered_dictionary = OrderedDict()

buyers = int(input())

for _ in range(buyers):
    x, y = input().rsplit(' ', 1)

    if x in ordered_dictionary:
        ordered_dictionary[x] = ordered_dictionary[x] + int(y)
    else:
        ordered_dictionary[x] = int(y)

for key, value in ordered_dictionary.items():
    print(key, value)