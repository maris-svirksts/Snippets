# https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    result = []

    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    [[[result.append([a, b, c]) for a in range(x + 1) if a + b+ c != n] for b in range(y + 1)] for c in range(z + 1)]
    
    print(sorted(result))
