import sys
input = sys.stdin.readline

class TreeNode:
    key = None
    left = None
    right = None

def createNode(key):
    node = TreeNode()
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

def insert(node, key):
    if node==None:
        return createNode(key)
    elif key > node.key:
        node.right = insert(node.right, key)
    elif key < node.key:
        node.left = insert(node.left, key)
    return node # 중복값은 보이지 않음

root = None
A = [35, 68, 35, 22, 17, 55, 30, 34, 65]

for a in A:
    root = insert(root, a)

preOrder(root)
print(" ")
inOrder(root)
print("")

if searchNode(root, 35):
    print("Found")
else:
    print("Not Found")