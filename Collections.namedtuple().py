from collections import namedtuple

n = int(input())
head =  ','.join(input().split())
Student =  namedtuple('Student',head)

sum_marks = 0
for i in range(n):
    row = input().split()
    student =  Student(*row)
    sum_marks += int(student.MARKS)

print(sum_marks/n)