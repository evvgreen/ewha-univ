INF = 100
N = 6

graph = [[0, 1, 2, 3, 4, 5],
        [1,0,4,2,5, INF],
        [2, INF, 0, 1, INF, 4],
        [3, 1, 3, 0, 1, 2],
        [4, -2, INF, INF, 0, 2],
        [5, INF, -3, 3, 1, 0]]
# 인접 행렬, 리스트
# 인접(정점간의 연결)

def floyd(graph):
    arr = graph
    for k in range(1, N):
        for i in range(1, N):
            for j in range(1, N):
                if (arr[i][k] + arr[k][j]) < arr[i][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]
        for a in arr:
            print(a)
        print("----")

floyd(graph)


"""
for k=1 to n
    for i=1 to n(i!=k)
        for j=1 to n(j!=k, j!=i)
            D[i,j] = min(D[i,k]+D[k,j], D[i,j])

"""