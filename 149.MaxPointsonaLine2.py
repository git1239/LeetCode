import numpy as np
from collections import Counter
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[8,4]]
points1 = [[1,1],[3,2],[5,3],[4,1],[2,3],[8,4]]
n = len(points)
D = []
def solver(x1,y1,x2,y2):
    if x2-x1 != 0:
        return (y2-y1)/(x2-x1)
for i in range(0,n-1):
    for j in range(1,n):
        d = solver(points[i][0],points[i][1],points1[j][0],points1[j][1])
        if d != None:
            D.append(d)
stats = Counter(D)
print(max(stats.values()))
