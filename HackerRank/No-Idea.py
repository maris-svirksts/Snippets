# https://www.hackerrank.com/challenges/no-idea/problem

input() # ignore: data not needed.

all_possible_elements       = input().split()
possible_happiness_elements = set(input().split())
possible_sadness_elements   = set(input().split())

happiness_elements = [elem for elem in all_possible_elements if elem in possible_happiness_elements]
sadness_elements = [elem for elem in all_possible_elements if elem in possible_sadness_elements]

print(len(happiness_elements) - len(sadness_elements))
