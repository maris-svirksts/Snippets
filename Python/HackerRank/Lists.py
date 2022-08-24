# https://www.hackerrank.com/challenges/python-lists/problem

number_of_commands = int(input())
commands           = []
placeholder        = []

# For < Python 3.10
for i in range(number_of_commands):
    command = input().split()
    command = [int(item) if item.isnumeric() else item for item in command]

    if command[0] == 'insert':
        placeholder.insert(command[1], command[2])
    elif command[0] == 'print':
        print(placeholder)
    elif command[0] == 'remove':
        placeholder.remove(command[1])
    elif command[0] == 'append':
        placeholder.append(command[1])
    elif command[0] == 'sort':
        placeholder.sort()
    elif command[0] == 'pop':
        placeholder.pop()
    elif command[0] == 'reverse':
        placeholder.reverse()