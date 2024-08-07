class Student:
    def __init__(self, name, subject1, subject2, subject3):
        self.name = name
        self.subject1, self.subject2, self.subject3 = subject1, subject2, subject3


n_students = int(input())
students = []

for _ in range(n_students):
    given_name, given_sub1, given_sub2, given_sub3 = tuple(input().split())
    students.append(
        Student(given_name, int(given_sub1), int(given_sub2), int(given_sub3))
    )

students.sort(key= lambda x: x.subject1 + x.subject2 + x.subject3)

for student in students:
    print(student.name, student.subject1, student.subject2, student.subject3)