"""Given the names and grades for each student in a Physics class of N
 students, store them in a nested list and print the name(s) of any
 student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their
names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, N, the number of students.
The  subsequent lines describe each student over 2N lines; the first
line contains a student's name, and the second line contains their
grade.

Constraints

    2 <= N <= 5

There will always be one or more students having the second lowest
grade.

Output Format

Print the name(s) of any student(s) having the second lowest grade
in Physics; if there are multiple students, order their names
alphabetically and print each one on a new line.
"""

from operator import itemgetter

def second_lowest(*args):
    arr = args[0]
    lowest, higher_lowest = arr[0], ["", 100]
    for student in arr:
        if student[1] < higher_lowest[1]:
            if student[1] < lowest[1]:
                higher_lowest, lowest = lowest, student
            elif student[1] == lowest[1]:
                continue
            else:
                higher_lowest = student
    return higher_lowest[1]


if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    second_largest_grade = second_lowest(students)
    result_list = list(filter(lambda x: x[1] == second_largest_grade, students))
    result_list.sort(key=itemgetter(0))
    for student in result_list:
        print(student[0])