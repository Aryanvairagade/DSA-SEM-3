
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root

def inorder(root):
    stack = []
    temp = root

    while temp or stack:
        while temp:
            stack.append(temp)
            temp = temp.left

        temp = stack.pop()
        print(temp.data, end=" ")
        temp = temp.right

def preorder(root):
    if root is None:
        return

    stack = [root]

    while stack:
        temp = stack.pop()
        print(temp.data, end=" ")

        if temp.right:
            stack.append(temp.right)

        if temp.left:
            stack.append(temp.left)

root = None

n = int(input("Enter number of nodes: "))

for i in range(n):
    data = int(input("Enter value: "))
    root = insert(root, data)

print("Inorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)
