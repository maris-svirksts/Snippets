# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

input_values = []

for i in range(4):
    raw = input().split()
    if i % 2 == 1:
        input_values.append(set(raw))

print(len(input_values[0].intersection(input_values[1])))