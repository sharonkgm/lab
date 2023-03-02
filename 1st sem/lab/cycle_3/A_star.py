from queue import PriorityQueue

#function for a* algorithm search
def A_star(graph,start, goal, h):
    cost = 0
    visited = []
    path =[]
    p_queue = PriorityQueue()
    p_queue.put((h[start], start))
	
    while p_queue:
        #assign a priority queue p
        p, current_node = p_queue.get()
        path.append(current_node)
        if current_node == goal:
            return path
        visited.append(current_node)
        for adjacent, new_cost in graph[current_node].items():
            if adjacent not in visited:
                cost = cost + new_cost
                p = h[adjacent] + cost
                p_queue.put((p, adjacent))
                cost = cost - new_cost
    return None

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

#assign hueristic values
h = {
	'A':5,
	'B':3,
	'C':10,
	'D':7
}

start = 'A'
goal = input("enter a goal to search :")
path = A_star(graph,start, goal, h)
#printing path cost
print("\nA* algorithm search of given graph is :\n")
for i in path:
     print(i,end = "->")
l = len(path)
i=1
cost = 0
while i < l :
    cost =cost + graph[path[i-1]][path[i]]
    i = i+1
print (f"\nTotal Path Cost : {cost} \n")
