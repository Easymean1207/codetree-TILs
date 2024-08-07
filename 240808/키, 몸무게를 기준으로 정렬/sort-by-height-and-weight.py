class Person:
    def __init__(self, name:str, height:int, weight:int):
        self.name, self.height, self.weight = name, height, weight


n_people = int(input())
people = []

for _ in range(n_people):
    given_name, given_height, given_weight = tuple(input().split())
    people.append(Person(given_name, int(given_height), int(given_weight)))

people.sort(key=lambda x:(x.height, -x.weight))

for person in people:
    print(person.name, person.height, person.weight)