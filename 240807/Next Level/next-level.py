class Character:
    def __init__(self, id ="codetree", level = 10):
        self.id = id
        self.level = level


user1 = Character()
print(f"user {user1.id} lv {user1.level}")

id, level = input().split()
level = int(level)

user2 = Character(id, level)
print(f"user {user2.id} lv {user2.level}")