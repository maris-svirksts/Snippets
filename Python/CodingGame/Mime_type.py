# https://www.codingame.com/ide/puzzle/mime-type

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

dict = {}

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt   = input().split()
    dict[ext.lower()] = mt

for i in range(q):
    inpt = input()

    try:
        data = inpt.split('.')
    except ValueError:
        print("UNKNOWN")
    else:
        print(dict[data[-1].lower()]) if data[-1].lower() in dict and len(data) > 1 else print("UNKNOWN")