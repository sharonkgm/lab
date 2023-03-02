#function for iterative deepening depth_first search
def iddfs(graph,visited,node,depth):
    for i in range(1,depth):
         visited = []
         if i != 1:
             print(f"\ndepth {i-1}")
        #calling dfs function
         dfs(graph,visited,node,i)

#function for depth_first search
def dfs(graph,visited,node,depth):
    depth = depth - 1 
    if depth == 0:
        return
    print (node,end ="->")
    visited.append(node)
    for adjacent in graph[node]:
         if adjacent not in visited:
            dfs(graph,visited,adjacent,depth)
    
graph = {'5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []}

depth = len(graph)
visited =set()
#calling iddfs function
iddfs(graph,visited ,'5',depth)
