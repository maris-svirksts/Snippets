# https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product

line_one = map(int, input().split())
line_two = map(int, input().split())

result = ' '.join(str(i) for i in list(product(line_one, line_two)))
print(result)