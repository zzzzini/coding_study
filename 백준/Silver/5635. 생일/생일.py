n = int(input())
students = []
for i in range(n):
    temp_students = input().split(' ')
    temp_students[1:] = map(int,temp_students[1:])
    students.append(temp_students)
students = sorted(students, key = lambda x : (x[3], x[2], x[1]))
print(students[-1][0])
print(students[0][0])