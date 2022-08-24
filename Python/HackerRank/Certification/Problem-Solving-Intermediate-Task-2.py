#!/bin/python3

import os
import re

#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#

def authEvents(events):
    result            = []
    M                 = (10 ** 9) + 7
    p                 = 131
    
    for i in events:
        if i[0] == 'setPassword':
            current_password  = 0
            possible_password = 0
            pass_length       = len(i[1])

            for s in i[1]:
                current_password  += ord(s) * (p ** (pass_length - 1))
                possible_password += ord(s) * (p ** (pass_length))
                pass_length -= 1

            current_password  = current_password % M
            possible_password = possible_password % M

        elif i[0] == 'authorize':
            if current_password == int(i[1]):
                result.append(1)
            else:
                possible_character = int(i[1]) - possible_password
                try:
                    if re.search(r"[a-zA-Z0-9]", chr(possible_character)):
                        result.append(1)
                    else:
                        result.append(0)
                except:
                    result.append(0)
                        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    events_rows = int(input().strip())
    events_columns = int(input().strip())

    events = []

    for _ in range(events_rows):
        events.append(input().rstrip().split())

    result = authEvents(events)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
