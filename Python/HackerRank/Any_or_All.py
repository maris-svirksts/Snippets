#! python

# https://www.hackerrank.com/challenges/any-or-all/problem

import math

def rev(num):
    return int(num != 0) and ((num % 10) * (10**int(math.log(num, 10))) + rev(num // 10))

def results():
    _          = input()
    numbers    = map(int, input().split())
    flag       = True
    palindrome = False

    for i in numbers:
        if i < 0:
            flag = False
            break
        elif not palindrome:
            palindrome = i == rev(i)

    if flag and palindrome:
        return True
    else:
        return False

# print(results())

#Reminder for two line solution (Taken from Discussions):
#N,n = int(raw_input()),raw_input().split()
#print all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n])