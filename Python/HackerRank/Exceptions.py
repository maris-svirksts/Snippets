counter = int(input())

for i in range(counter):
    try:
        first, second = map(int, input().split())
        print(int(first/second))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except Exception as e:
        print("Error Code: {}".format(e))