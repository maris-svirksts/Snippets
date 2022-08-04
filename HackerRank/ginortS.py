unsorted_string = input()

lower_case = []
upper_case = []
odd_digits = []
even_digits = []

for i in unsorted_string:
    if i.isdigit():
        if int(i) % 2 == 0:
            even_digits.append(i)
        else:
            odd_digits.append(i)
    elif i.isupper():
        upper_case.append(i)
    else:
        lower_case.append(i)



result = "".join(sorted(lower_case) + sorted(upper_case) + sorted(odd_digits) + sorted(even_digits))

print(result)