from typing import List

class Person:
    def __init__(self, name:str, height:int, weight:float):
        self.name, self.height, self.weight = name, height, weight


def sortByName(input_people:List[Person]) -> None:
    input_people.sort(key= lambda x:x.name)
    
    print('name')
    for input_person in input_people:
        print(input_person.name, input_person.height, round(input_person.weight,1))


def sortByHeight(input_people:List[Person]) -> None:
    input_people.sort(key=lambda x:-x.height)
    
    print('height')
    for input_person in input_people:
        print(input_person.name, input_person.height, round(input_person.weight,1))


n_people = 5
people = []

for _ in range(n_people):
    given_name, given_height, given_weight = tuple(input().split())
    people.append(Person(given_name, int(given_height), float(given_weight)))

sortByName(people)
print()
sortByHeight(people)