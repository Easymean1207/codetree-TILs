from typing import List

class Coordinate:
    def __init__(self, x:int, y:int, num:int):
        self.x,self.y = x,y
        self.num = num

# 원점 기준 맨허튼 거리를 계산하는 함수
def calculateManhattan(points:List[Coordinate]) -> None:
    points.sort(key= lambda p: abs(p.x)+abs(p.y))


number_of_points = int(input())
points = []

for i in range(number_of_points):
    given_x, given_y = tuple(map(int, input().split()))
    given_num = i+1
    points.append(Coordinate(given_x, given_y, given_num))

calculateManhattan(points)

for point in points:
    print(point.num)