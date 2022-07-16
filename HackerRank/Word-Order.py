# https://www.hackerrank.com/challenges/word-order/problem

line_count = int(input())
word_list = {}

for i in range(line_count):
    word = input()
    word_list[word] = word_list.get(word, 0) + 1

print(len(word_list))
print(" ".join(map(str, list(word_list.values()))))

