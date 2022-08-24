#! python

# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))

number_of_commands = int(input())
commands = []

# For >= Python 3.10
for i in range(number_of_commands):
    command = input().split()
    match command[0]:
        case 'pop':
            s.pop()
        case 'remove':
            s.remove(int(command[1]))
        case 'discard':
            s.discard(int(command[1]))
        case _:
            print("Unknown command", command[0])

# For < Python 3.10
for i in range(number_of_commands):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))
        
print(sum(s))