class Character:
    def __init__(self, id ="", level = 0):
        self.id = id
        self.level = level


user1 = Character("codetree", 10)
print(f"user {user1.id} lv {user1.level}")

id, level = input().split()
level = int(level)

user2 = Character(id, level)
print(f"user {user2.id} lv {user2.level}")