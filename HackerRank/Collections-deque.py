# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque
s = deque()

number_of_commands = int(input())
commands = []

# For >= Python 3.10
for i in range(number_of_commands):
    command = input().split()
    match command[0]:
        case 'pop':
            s.pop()
        case 'append':
            s.append(command[1])
        case 'popleft':
            s.popleft()
        case 'appendleft':
            s.appendleft(command[1])
        case _:
            print("Unknown command", command[0])

# For < Python 3.10
for i in range(number_of_commands):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'append':
        s.append(command[1])
    elif command[0] == 'popleft':
        s.popleft()
    elif command[0] == 'appendleft':
        s.appendleft(command[1])
        
print(" ".join(s))