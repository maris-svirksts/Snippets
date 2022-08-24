#!python

# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        print("{:{align}{width}} {:{align}{width}} {:{align}{width}} {:{align}{width}}".format(i, oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:], align='>', width=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)