#! python

# https://www.hackerrank.com/challenges/sherlock-and-array/problem

import os

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    total_sum = sum(arr)
    left_side = 0

    for i in arr:
        if left_side == total_sum - i - left_side:
            return 'YES'
        else:
            left_side += i
    
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
