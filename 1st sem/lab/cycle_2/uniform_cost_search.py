from queue import PriorityQueue

#function to perform uniform cost search
def ucs(start,goal,graph):
    p_queue = PriorityQueue()
    #set priority queue with two values cost and node
    p_queue.put((0,start))
    visited =set()
    while p_queue:
        cost, current_node = p_queue.get()
        if current_node == goal:
            return cost
        visited.add(current_node)
        for adjacent, new_cost in graph[current_node].items():
            if adjacent not in visited:
                #calculate the cost
                total_cost = cost + new_cost
                p_queue.put((total_cost,adjacent))
    return None
            


#input graph with node and cost
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start = 'A'
goal = input("enter the goal node :")
#function calling to perform uniform cost search
result = ucs(start,goal,graph)
print(f"\nuniform cost search of the graph start from {start} to {goal} is : ",result)