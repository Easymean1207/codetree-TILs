class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor, self.eng, self.math = kor, eng, math


n_students = int(input())
students = []

for _ in range(n_students):
    name, kor, eng, math = tuple(input().split())
    students.append(Student(name, int(kor), int(eng), int(math)))

# 우선 순위는 kor > eng > math
# 점수가 높은 순서대로 나열하므로 내림차순으로 정렬
students.sort(key= lambda x:(-x.kor, -x.eng, -x.math))

for student in students:
    print(student.name, student.kor, student.eng, student.math)