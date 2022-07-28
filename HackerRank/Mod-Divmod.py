#! python

# https://www.hackerrank.com/challenges/python-mod-divmod/problem

first_element  = int(input())
second_element = int(input())

result = divmod(first_element, second_element)

print(result[0])
print(result[1])
print(result)