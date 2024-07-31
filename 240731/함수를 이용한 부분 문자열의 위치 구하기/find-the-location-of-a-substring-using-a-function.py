def findGoal(source, goal):
    idx = source.find(goal)
    return idx   


source = input()
goal = input()

result = findGoal(source, goal)
print(result)