# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# Can be changed to 4 lines or less, looks ugly.

from collections import namedtuple

Students = []
result   = 0

counter, Student = int(input()), namedtuple('Student', input().split())

[Students.append(Student._make(input().split())) for _ in range(counter)]

for x in Students:
    result += int(x.MARKS)

print(round(result / len(Students), 2))
