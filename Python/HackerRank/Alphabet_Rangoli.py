#! python

# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    # your code goes here
    # the alphabet
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    # create a list of dashes and letters, and join them into a string
    L = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1]+s[1:]).center(4*size-3, "-"))
        
    # print the top part of the rangoli, the middle line, and then the bottom part (which is just the reverse of the top part)
    print('\n'.join(L[:0:-1]+L))
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)