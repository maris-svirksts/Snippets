#!python

# https://www.hackerrank.com/challenges/python-sort-sort/problem

from operator import itemgetter

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])

    unsorted_list = []

    for _ in range(n):
        unsorted_list.append(list(map(int, input().rstrip().split())))

    sort_key = int(input())

    sorted_list = sorted(unsorted_list, key = itemgetter(sort_key))

    for element in sorted_list:
        print(' '.join(str(e) for e in element))
