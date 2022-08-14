#!python

# https://www.hackerrank.com/challenges/py-check-subset/problem

input_counter = int(input())

for _ in range(input_counter):
    _ = input()
    first_element = set(map(int, input().split()))
    _ = input()
    second_element = set(map(int, input().split()))

    print(first_element.issubset(second_element))