class Student:
    def __init__(self, height, weight, number):
        self.height, self.weight = height, weight
        self.number = number

n_students = int(input())
students = []

for i in range(1, n_students+1):
    given_height, given_weight = tuple(map(int, input().split()))
    given_number = i
    students.append(Student(given_height, given_weight, given_number))

students.sort(key= lambda x:(x.height, -x.weight))

for student in students:
    print(student.height, student.weight, student.number)