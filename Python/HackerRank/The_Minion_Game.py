#! python

# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    # your code goes here
    # initialize scores
    vowels = 'AEIOU'
    kev_sc = 0
    stu_sc = 0
    
    for i in range(len(s)):
        if s[i] in vowels:
            kev_sc += (len(s)-i)
        else:
            stu_sc += (len(s)-i)
    
    # check who won
    if kev_sc > stu_sc:
        print("Kevin", kev_sc)
    elif kev_sc < stu_sc:
        print("Stuart", stu_sc)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)