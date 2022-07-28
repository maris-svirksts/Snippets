#! python

# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem

number_of_commands = int(input())
commands = []
data_holder = []

# If statements instead of switch because Hackerrank Python version doesn't support switch statements.
for i in range(number_of_commands):
    command = input().split()
    if command[0] == '1':
        data_holder.append(command[1])
    elif command[0] == '2':
        data_holder.pop(0)
    elif command[0] == '3':
        print(data_holder[0])