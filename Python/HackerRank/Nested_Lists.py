# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name  = input()
        score = float(input())
        
        students.append([name, score])
    
    students.sort(key = lambda tup: tup[1])

    without_lowest = list(filter(lambda student: student[1] != students[0][1], students))
    result_list    = list(filter(lambda student: student[1] == without_lowest[0][1], without_lowest))
    
    result_list.sort(key = lambda tup: tup[0])

    [print(student[0]) for student in result_list]
