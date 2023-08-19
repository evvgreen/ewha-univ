import sys
input = sys.stdin.readline

def SWAP(x, y):
    temp = x
    x = y
    y = temp
    return x, y

def bubbleSort(A):
    print("before:", A)
    N = len(A)
    for p in range(1, N):
        flag = False

        for i in range(1, N-p+1):
            if A[i-1] > A[i]:
                A[i-1], A[i] = SWAP(A[i-1], A[i])
                flag = True
        
        if flag == False:
            break
        print(p, "pass>>", A)

A = [40, 10, 50, 90, 20, 80, 30, 60]
# 정렬된 후 +1 번 돌고 더는 돌지 않음

bubbleSort(A)

"""
for pass=1 to n-1
    for i=1 to n-pass
    if(A[i-1]>A[i])
        SWAP(A[i-1], A[i])
return A
"""