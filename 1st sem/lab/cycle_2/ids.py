def iddfs(graph,visited,node,depth):
    for i in range(1,depth):
         visited = []
         if i != 1:
             print(f"\ndepth {i-1}")
         dfs(graph,visited,node,i)
        
def dfs(graph,visited,node,depth):
    depth = depth - 1 
    if depth == 0:
        return
    print (node,end ="->")
    visited.append(node)
    for neighbour in graph[node]:
         if neighbour not in visited:
            dfs(graph,visited,neighbour,depth)
    
graph = {'5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []}


depth = len(graph)
visited =set()
iddfs(graph,visited ,'5',depth)