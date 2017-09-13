from collections import defaultdict

def DFS(G,v,seen=None,path=None):
    if seen is None: seen = []
    if path is None: path = [v]

    seen.append(v)

    paths = []
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(DFS(G, t, seen[:], t_path))
    return paths


# Define graph by edges
edges = [['5', '6'], ['2', '2'], ['1', '1'], ['3', '3'],['2','3'],['1','4'],['3','4']]

# Build graph dictionary
G = defaultdict(list)
for (s,t) in edges:
    G[s].append(t)
    G[t].append(s)
print(G)

q=[]
for i in range(1,6):
    all_paths = DFS(G, str(i))
    max_len   = max(len(p) for p in all_paths)
    max_paths = [p for p in all_paths if len(p) == max_len]
    q.append(max_len)
# Output
print("All Paths:")
print(all_paths)
print("Longest Paths:")
for p in max_paths: print("  ", p)
print("Longest Path Length:")
print(max_len)
print(q)
