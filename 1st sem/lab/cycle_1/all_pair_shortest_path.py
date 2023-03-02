#set a infinit value to INF when there is no path between that nodes
INF = 9999   
#function to print solution
def solution(vertices, distance):
    for i in range(vertices):
        for j in range(vertices):
            if(distance[i][j] != INF):
                print(distance[i][j], end="  ")
            else:
                print("INF", end=" ")
        print(" ")

#function to find shortest path between all node pair
def shortest_path(vertices, graph):
    distance = graph
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print("\nall pair shortest path of given graph :\n")
    solution(vertices, distance)


graph = [[0, 8, INF, 1],
     [INF, 0, 1, INF],
     [4, INF, 0, INF],
     [INF, 2, 9, 1]
     ]

shortest_path(4, graph)