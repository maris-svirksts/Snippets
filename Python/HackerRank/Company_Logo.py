# https://www.hackerrank.com/challenges/most-commons/problem

if __name__ == '__main__':
    s = input()
    
    counter = {}
    
    for x in s:
        if x in counter:
            counter[x] += 1
        else:
            counter[x] = 1

    [print(k, v) for k, v in sorted(counter.items(), key = lambda item: (-item[1], item[0]))[:3]]