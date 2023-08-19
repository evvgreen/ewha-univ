import sys
input = sys.stdin.readline

def SWAP(x, y):
    temp = x
    x = y
    y = temp
    return x, y

def insertionSort(A):
    print("before:", A)
    N = len(A)

    for i in range(1, N):
        currentElement = A[i]
        j = i-1
        while(j>=0 and A[j] > currentElement):
            A[j+1] = A[j]
            j-=1
        A[j+1] = currentElement

        print(i, A)

A = [40, 10, 50, 90, 20, 80, 30, 60]
insertionSort(A)