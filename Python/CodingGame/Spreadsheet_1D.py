# https://www.codingame.com/ide/puzzle/1d-spreadsheet

import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def calculate(key):
    try:
        return int(key)
    except:
        if 'VALUE' == dict[key][0]:
            value = calculate(dict[key][1])
            return value
        elif 'ADD' == dict[key][0]:
            result = calculate(dict[key][1]) + calculate(dict[key][2])
        elif 'SUB' == dict[key][0]:
            result = calculate(dict[key][1]) - calculate(dict[key][2])
        elif 'MULT' == dict[key][0]:
            result = calculate(dict[key][1]) * calculate(dict[key][2])

        dict.update({key: ('VALUE', result, '_')})
        return result

n    = int(input())
dict = {}

for i in range(n):
    dict['$' + str(i)] = (operation, arg_1, arg_2) = input().split()

for key in dict:
    print(calculate(key))