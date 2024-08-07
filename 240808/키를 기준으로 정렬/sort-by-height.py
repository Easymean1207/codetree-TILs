class Person:
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight


n = int(input())
people = []

# 받은 정보를 Person Class의 형태로 people에 추가 
for _ in range(n):
    given_name, given_height, given_weight = tuple(input().split())
    given_height, given_weight = int(given_height), int(given_weight)
    people.append(Person(given_name, given_height, given_weight))

# 키를 기준으로 오름차순 정렬
people.sort(key=lambda x: x.height)

for person in people:
    print(person.name, person.height, person.weight)