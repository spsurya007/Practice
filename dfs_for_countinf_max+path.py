from collections import defaultdict

a,b=map(int,input().split(" "))
edges=[]
for i in range(b):
    edges.append(list(map(str,input().split())))

def DFS(G,v,seen=None,path=None):
    if seen is None: seen = []
    if path is None: path = [v]
    seen.append(v)
    paths = []
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            paths.append(list(t_path))
            paths.extend(DFS(G, t, seen[:], t_path))
    return paths
G = defaultdict(list)
for (s,t) in edges:
    G[s].append(t)
    G[t].append(s)
print((G))
q=[]
m=[]
for (s,t) in edges :
    m.append(s)
m=list(set(m))
print(m)
for i in m:
    all_paths = DFS(G,i)
    print(all_paths)
    sum=[]
    for  x in range(len(all_paths)):
        sum+=all_paths[x]
    sum=list(set(sum))
    if len(sum)!=0:
        q.append(len(sum))
    else:q.append(1)
print(q)
print(max(q))