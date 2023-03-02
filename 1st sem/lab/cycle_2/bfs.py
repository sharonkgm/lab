graph = {'5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []}

visited = []
queue = []
#function for breadth first search
def bfs(visited,graph, start_node):
    visited.append(start_node)
    queue.append(start_node)
    while queue:
        node =queue.pop(0)
        print(node, end = "->")
        for adjacent in graph[node]:
            if adjacent not in visited:
                visited.append(adjacent)
                queue.append(adjacent)

print("\nbreadth first search of the given graph :")
#calling function for breadth first search
bfs(visited,graph,'5')