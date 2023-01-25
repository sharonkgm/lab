graph = {'1':['2','3'],'2':['3','4'],'3':['4'],'4':['5'],'5':[]}
v = []
q = []

def bfs(v,graph, n):
    v.append(n)
    q.append(n)
    while q:
        m =q.pop(0)
        print(m, end = " ")
        for i in graph[m]:
            if i not in v:
                v.append(i)
                q.append(i)

print("bfs of the given graph :")
bfs(v,graph,'2')