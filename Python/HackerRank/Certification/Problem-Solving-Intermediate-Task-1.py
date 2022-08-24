#!/bin/python3

import os

#
# Complete the 'taskOfPairing' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY freq as parameter.
#

def taskOfPairing(freq):
    total      = 0
    bleed_over = 0

    for i in freq:
        actual = i + bleed_over

        if i == 0:
            bleed_over = 0
            continue
        elif actual % 2 == 1:
            total += (actual - 1) / 2
            bleed_over = 1
        else:
            total += actual / 2
            bleed_over = 0
    
    return int(total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    freq_count = int(input().strip())

    freq = []

    for _ in range(freq_count):
        freq_item = int(input().strip())
        freq.append(freq_item)

    result = taskOfPairing(freq)

    fptr.write(str(result) + '\n')

    fptr.close()
