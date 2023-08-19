import sys
input = sys.stdin.readline

def SWAP(x, y):
    temp = x
    x = y
    y = temp
    return x, y

def shellSort(A, gap):
    print("before:", A)
    N = len(A)

    for h in range(gap, 0, -2):
        for i in range(h, N):
            currentElement = A[i]
            j = i 
            while(j>=h and A[j-h] > currentElement):
                A[j] = A[j-h]
                j -= h
            A[j] = currentElement
        
        print(h, i, A)


A = [30, 60, 90, 10, 40, 80, 40, 20, 10, 60, 50, 30, 40, 90, 80]
shellSort(A, 5)


"""
for each gap h = [큰 갭부터 차례로]
    for i=h to n-1
    CurrentElement = A[i]
    j=i
    while (j>=h) and (A[j-h]> CurrentElement)
        A[j]=A[j-h]
        j=j-h
    A[j] = CurrentElement
"""