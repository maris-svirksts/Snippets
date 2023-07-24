#! python

# https://www.hackerrank.com/challenges/designer-door-mat/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int,input().split()) # reading the input

# print the top pattern
for i in range(1, N, 2):
    print((i * ".|.").center(M, "-"))
    
# print the "WELCOME" part
print("WELCOME".center(M, "-"))

# print the bottom pattern, which is just the reverse of the top pattern
for i in range(N-2, -1, -2):
    print((i * ".|.").center(M, "-"))
