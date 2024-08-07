class Resident:
    def __init__(self, name:str, street_number:int, location:str):
        self.name = name
        self.street_number = street_number
        self.location = location


n = int(input())

residents = []
for _ in range(n):
    given_name, given_street_number, given_location = tuple(input().split())
    residents.append(Resident(given_name, given_street_number, given_location))

residents.sort(key = lambda x: x.name)
last_resident = residents[-1]

print(f"name {last_resident.name}")
print(f"addr {last_resident.street_number}")
print(f"city {last_resident.location}")