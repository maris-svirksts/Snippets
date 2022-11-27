# https://www.hackerrank.com/challenges/symmetric-difference/problem

_, a = input(), set(map(int, input().split()))
_, b = input(), set(map(int, input().split()))

[print(i) for i in sorted(b.difference(a).union(a.difference(b)))]
