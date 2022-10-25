# https://www.codingame.com/ide/puzzle/telephone-numbers

n = int(input())
elements = set()

for _ in range(n):
    telephone = input()

    for i in range(len(telephone)):
        elements.add(telephone[:i + 1])

# The number of elements (referencing a number) stored in the structure.
print(len(elements))
