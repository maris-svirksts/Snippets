#! python

# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: x ** 3 # complete the lambda function 

def fibonacci(n):
    result = [0, 1]

    for i in range(2, n):
        result.append(result[i - 1] + result[i - 2])

    return result[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))