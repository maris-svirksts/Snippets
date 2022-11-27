from collections import defaultdict
d = defaultdict(list)

A, B = input().split()

#[d[input()].append(str(i + 1)) for i in range(int(A))]
for i in range(int(A)):
    d[input()].append(str(i + 1))

for _ in range(int(B)):
    key = input()

    if key not in d:
        print('-1')
    else:
        print(' '.join(d[key]))
