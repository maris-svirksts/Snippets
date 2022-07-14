#! python

# https://www.hackerrank.com/challenges/py-set-add/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    z = ["alpha","bravo","charlie"]
    new_z = [i[0]*2 for i in z]
    print(new_z)

    i = 0
    number_of_countries = int(input())
    unique_countries = set()

    while i < number_of_countries:
        unique_countries.add(input())
        i += 1
    
    print(len(unique_countries))