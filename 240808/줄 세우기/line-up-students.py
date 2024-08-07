class Student:
    def __init__(self, height, weight, number):
        self.height, self.weight = height, weight
        self.number = number


n_students = int(input())
students = []

for i in range(n_students):
    given_height, given_weight = tuple(map(int, input().split()))
    given_number = i+1
    students.append(Student(given_height, given_weight, given_number))

# 정렬 우선순위 : 키(내림차순) > 몸무게(내림차순) > 번호(오름차순)
students.sort(key= lambda x: (-x.height, -x.weight, x.number))

for student in students:
    print(student.height, student.weight, student.number)