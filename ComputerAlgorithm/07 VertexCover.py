g = [[0, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 0]]

def VertexCover(adj):
    V = len(adj)
    visited = [False]*V
    c = []

    for u in range(V):
        if visited[u] == False:
            for v in range(V):
                if adj[u][v] != 0 and visited[v] == False:
                    c.append(u)
                    c.append(v)
                    visited[u] = True
                    visited[v] = True
                    break
    return c

c = VertexCover(g)
print('Vertex Cover = ', c)