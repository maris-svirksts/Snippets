#! python

# https://www.hackerrank.com/challenges/piling-up/problem

def check_list(block, old):
    while len(block) > 0:
        if block[0] <= old and block[-1] <= block[0]:
            old = block.pop(0)
        elif block[-1] <= old:
            old = block.pop()
        elif block[0] <= old:
            old = block.pop(0)
        else:
            break

    return block


input_values = []

element_count = int(input())

for i in range(element_count * 2):
    raw = input().split()
    if i % 2 == 1:
        input_values.append(list(map(int, raw)))

for block in input_values:
    if block[0] >= block[-1]:
        old = block.pop(0)
    else:
        old = block.pop()
    
    result = check_list(block, old)

    if len(result) == 0:
        print("Yes")
    else:
        print("No")