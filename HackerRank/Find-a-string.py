#! python

# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    result = recursive_search(string, sub_string, 0, 0)

    return result

def recursive_search(string, substring, count, start):
    position = string.find(substring, start)

    if position < 0:
        return count
    else:
        count += 1
        return recursive_search(string, substring, count, position + 1)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)