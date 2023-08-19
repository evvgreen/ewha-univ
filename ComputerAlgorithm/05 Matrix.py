import sys
input = sys.stdin.readline

# 열과 행의 수가 같아야 함 (열 * 행)

INF = 10000
N = 5

D = [10, 20, 5, 15, 30]
C = [[0 for i in range(N)] for i in range(N)]

def matrixChain(C, D):
    for L in range(1, N-1):
        for i in range(1, N-L):
            j = i + L
            C[i][j] = INF

            for k in range(i, j):
                temp = C[i][k] + C[k+1][j] + D[i-1]*D[k]*D[j]
                if temp < C[i][j]:
                    C[i][j] = temp
        for c in C:
            print(c)
        print("---")

matrixChain(C, D)

"""
for i=1 to n
    C[i, i] = 0 # 자기 자신은 곱하지 않음

# i는 행, j는 열, 대각선으로 표의 위쪽 부분만 씀

for L = 1 to n-1
    for i=1 to n-L
        j = i+L
        C[i, j] = INF
        for k=i to j-1
            temp = C[i,k] + C[k+1, j] + d[i-1]*[k]*[j]
            if temp < C[i, j]
                C[i, j] = temp
return C[1, n]
"""