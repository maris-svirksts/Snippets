#!python

# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

super_set     = set(map(int, input().split()))
input_counter = int(input())
flag          = "True"

for _ in range(input_counter):
    set_to_check = set(map(int, input().split()))

    if not set_to_check.issubset(super_set) and super_set is not set_to_check:
        flag = "False"
        break

print(flag)
