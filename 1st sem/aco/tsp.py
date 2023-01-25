from sys import maxsize
from itertools import permutations

def tsp(graph,start):
    vertex = []
    path = []
    l = len(graph)
    for i in range(l):
        if i != start:
            vertex.append(i)
    min_path = maxsize
    permutation2 = permutations(vertex)
    for i in permutation2:
        current_path = 0
        b = start
        for j in i:
            current_path += graph[b][j]
            b = j
        current_path += graph[b][start]
    if min_path > current_path:
        min_path = current_path
        path.append(i)
    return min_path,path



graph = [[0,10,5,11],
         [6,0,12,8],
         [5,12,0,25],
         [11,8,25,0]]
start = 0
c = tsp(graph, start)

print(f'minimum cost :{c[0]}')
for i in c[1]:
    print(f'minimum path :{start}{i}{start}')
