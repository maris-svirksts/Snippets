#! python

# https://www.hackerrank.com/challenges/zipped/problem

temp, line_count = input().split()

elements = []

for i in range(int(line_count)):
    elements.append(list(map(float, input().split())))

zipped = zip(*elements)

for i in zipped:
    print(round(sum(i) / len(i), 2))