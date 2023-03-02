graph = {'5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []}
#Set to keep track of visited nodes of graph.
visited = set() 
#function for depth first search
def dfs(visited, graph, node):   
    if node not in visited:
        print(node,end = "->")
        visited.add(node)
        for adjacent in graph[node]:
            #recursive calling of function
            dfs(visited, graph, adjacent)

print("Depth-First Search of given graph :\n")
#calling function
dfs(visited, graph, '5')