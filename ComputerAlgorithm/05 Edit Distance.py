import sys
input = sys.stdin.readline

N = 100
S = "strong"
T = "stone"

def editDistance(S, T, m, n):
    E = [[N for i in range(n+1)] for i in range(m+1)]
    for j in range(n+1):
        E[0][j] = j
    for i in range(m+1):
        E[i][0] = i
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if S[i-1] == T[j-1]:
                E[i][j] = E[i-1][j-1]
            else:
                E[i][j] = min(E[i][j-1], E[i-1][j], E[i-1][j-1]) + 1 # 세로 삭제, 가로 삽입, 대각선 대체
        for e in E:
            print(e)
        print("---")

editDistance(S, T, len(S), len(T))