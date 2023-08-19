import sys
input = sys.stdin.readline
N = 100

class HeapType:
    def __init__(self):
        self.heap = [0 for n in range(N)]
        self.heapSize = 0

def downHeap(pH):
    item = pH.heap[1]
    parent = 1
    child = 2
    while(child<=pH.heapSize):
        if( (child< pH.heapSize) and (pH.heap[child+1] > pH.heap[child])):
            child+=1

        if item >= pH.heap[child]:
            break

        pH.heap[parent] = pH.heap[child]
        parent = child
        child = child*2
    pH.heap[parent] = item
    

def heapSort(H):
    pH = H
    n = pH.heapSize
    for i in range(1, n+1):
        item = pH.heap[1]
        pH.heap[1] = pH.heap[pH.heapSize]
        pH.heap[pH.heapSize] = item
        pH.heapSize -= 1
        downHeap(pH)
        print(i, pH.heap[1:n+1])


def upHeap(pH):
    i = pH.heapSize
    key = pH.heap[i]
    while(i!=1 and key > pH.heap[i//2]):
        pH.heap[i] = pH.heap[i//2]
        i = i//2
    pH.heap[i] = key

def printHeap(pH):
    print(pH.heap[1:pH.heapSize+1])

def insertItem(pH, key):
    pH.heapSize += 1
    pH.heap[pH.heapSize] = key
    upHeap(pH)

A = [90, 60, 80, 50, 30, 70, 10, 20, 40]

H = HeapType()
for a in A:
    insertItem(H, a)

printHeap(H)
heapSort(H)
# insertItem(H, 80)
# printHeap(H)