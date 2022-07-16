# https://www.hackerrank.com/challenges/compress-the-string/problem

input_string = input()

current_character = ""
end_string        = ""
count             = 0

for i in input_string:
    if i != current_character:
        if current_character != "":
            end_string += "({}, {}) ".format(count, current_character)
        current_character = i
        count = 1
    else:
        count += 1

end_string += "({}, {})".format(count, current_character)
print(end_string)