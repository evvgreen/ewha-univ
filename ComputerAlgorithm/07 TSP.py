tree = [[1, 3, 4], [0, 2], [1, 5], [0], [0], [2]]
n = len(tree)
INF = float('inf')
g = [[0, 3, INF, 2, 4, INF],
    [3, 9, 1, 4, INF, 2],
    [INF, 1, 0, INF, INF, 1],
    [2, 4, INF, 0, 5, 7],
    [4, INF, INF, 5, 0, 9],
    [INF, 2, 1, 7, 9, 0]]

visited = [False for _ in range(n)]
path = []

def dfs(v):
    visited[v] = True
    path.append(v)
    for w in tree[v]:
        if not visited[w]:
            dfs(w)
            path.append(v)

dfs(0)
print("트리 방문 순서: ", path)
s = []
for vertex in path:
    if vertex not in s:
        s.append(vertex)
s.append(0)
print('TSP 경로:', s)

dist = 0
for i in range(n):
    dist += g[s[i]][s[i+1]]
print('appr dist =', dist)