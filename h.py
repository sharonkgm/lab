

def iterativedeepening(graph, node, visited, depth):
    for i in range(1, depth):
        visited = [False]*limit
        print("\nUpdating Depth.")
        Dfs(graph, node, visited, i)
                
def Dfs(graph, node, visited, depth):
    depth = depth -1 
    if depth == 0:
        return
    print(node, end=" >> ")
    visited[node] = True
    for next in graph[node]:
        #depth = depth -1
        if visited[next] == False:
            #depth = depth - 1
            Dfs (graph, next, visited, depth)
    
#graph

graph = {5 : ['3','7'],
  3 : ['2', '4'],
  7 : ['8'],
  2 : [],
  4 : ['8'],
  8 : []}

print (f"\nGraph :\n")
for element in graph:
    print (f"{element} :{graph[element]} \n")

start = 5
limit = len(graph)
visited = []
iterativedeepening(graph, start, visited, limit)