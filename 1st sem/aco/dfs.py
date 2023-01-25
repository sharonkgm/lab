graph = {'1':['3','2'],'2':['3','4'],'3':['4'],'4':['5'],'5':[]}
#graph = {'0':['3','2','1'],'1':[],'2':['4'],'4':[],'3':[]}
v = []
s = []
def dfs(v,graph,n):
    v.append(n)
    s.append(n)
    while s:
        m =s.pop()
        print(m, end = " ")
        for i in graph[m]:
            if i not in v:
                v.append(i)
                s.append(i)





print("dfs of the given graph :")
dfs(v,graph,'1')
