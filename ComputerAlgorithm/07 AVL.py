import sys
input = sys.stdin.readline

class AVLNode:
    key = None
    left = None
    right = None

def createNode(key):
    node = AVLNode()
    node.key = key
    return node

def preOrder(root):
    if root!=None:
        print(root.key, end=' ')
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if root!=None:
        preOrder(root.left)
        print(root.key, end=' ')
        preOrder(root.right)

def searchNode(node, key):
    if node==None:
        return None
    elif key == node.key:
        return node
    elif key < node.key:
        return searchNode(node.left, key)
    elif key > node.key:
        return searchNode(node.right, key)

def getHeight(node):
    height = 0
    if node != None:
        height = 1 + max(getHeight(node.left), getHeight(node.right))
    return height

def getBalance(node):
    if(node==None):
        return 0
    return getHeight(node.left) - getHeight(node.right)

def rotateRight(p):
    c = p.left
    p.left = c.right
    c.right = p
    return c

def rotateLeft(p):
    c = p.right
    p.right = c.left
    c.left = p
    return c

def insert(node, key):
    if node==None:
        return createNode(key)
    elif key > node.key:
        node.right = insert(node.right, key)
    elif key < node.key:
        node.left = insert(node.left, key)

    balance = getBalance(node)

    left = node.left
    right = node.right
    if (balance > 1 and key<left.key): #LL
        node =  rotateRight(node)
    if (balance > 1 and key>left.key): #LR
        node.left = rotateLeft(node.left)
        node = rotateRight(node)
    if( balance < -1 and key<right.key): #RL
        node.right = rotateRight(node.right)
        node = rotateLeft(node)
    if (balance < -1 and key>right.key): #RR
        node = rotateLeft(node)

    return node # 중복값은 보이지 않음

root = None
A = [35, 25, 13, 40, 45, 30]

for a in A:
    root = insert(root, a)
    preOrder(root)
    print(" ")

preOrder(root)
print(" ")
inOrder(root)
print("")

if searchNode(root, 35):
    print("Found")
else:
    print("Not Found")