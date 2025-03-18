""" find the runner up score!"""
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    l = []
    for i in arr:
        if i not in l:
            l.append(i)
    l.sort()
    if len(l) >= 2:
        print(l[-2])

""" You are given a string .
Your task is to find the first occurrence of an alphanumeric character in S(read from left to right) that has consecutive repetitions."""
def frist_find(s):
    for i in range(len(s)-1):
        if s[i].isalnum() and s[i] == s[i + 1]:
            return s[i]
    return -1
    
s = input().strip()
result = frist_find(s)
print(result)

""" Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line."""
if __name__ == '__main__':
    students = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    sort = sorted(list(set(grade for name, grade in students)))
    m = []
    if len(sort) >= 2:
        for i in sort:
            if i not in m:
                m.append(i)
        m.sort()
        sort = m[1]
        second_lowest_students = [i for i in students if i[1] == sort]
        length = len(second_lowest_students)
        for i in range(length - 1, -1, -1):
            print(second_lowest_students[i][0])