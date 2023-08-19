import sys
input = sys.stdin.readline

A = [40, 10, 50, 90, 20, 80, 30, 60]

def SWAP(x, y):
    temp = x
    x = y
    y = temp
    return x, y

def selectionSort(A):
    print("before:", A)
    N = len(A)

    for i in range(N-1):
        min = i
        for j in range(i+1, N):
            if A[j] < A[min]:
                min = j
        A[i], A[min] = SWAP(A[i],A[min])
        print(i+1, A)

#selectionSort(A)

def selectionSortReverse(A):
    print("before:", A)
    N = len(A)

    for i in range(N-1):
        max = 0
        for j in range(1, N-i):
            if A[j] > A[max]:
                max = j
        A[N-1-i], A[max] = SWAP(A[N-1-i],A[max])
        print(i+1, A)

selectionSortReverse(A)


"""
for i=0 to n-2
    min=i
    for j=i+1 to n-1
        if A[j]<A[min]
            min=j
    SWAP(A[i], A[min])
return A
"""