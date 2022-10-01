# https://www.hackerrank.com/challenges/python-quest-1/problem

elements = map(lambda x: print(sum([x * (10 ** y) for y in range(x)])), range(1, int(input())))
list(elements) # Trigers the print call from above line.