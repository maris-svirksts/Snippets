#! python

# https://www.hackerrank.com/challenges/merge-the-tools/problem

import re

def merge_the_tools(string, k):
    # your code goes here
    regex = ".{1," + str(k) + "}"
    divided_list = re.findall(regex, string)

    for element in divided_list:
        unique_characters = ""
        for character in element:
            if character not in unique_characters:
                unique_characters += character
        print(unique_characters)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)