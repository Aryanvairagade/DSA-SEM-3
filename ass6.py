
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

def level_order(root):
    if root is None:
        return

    queue = [root]

    while queue:
        temp = queue.pop(0)
        print(temp.data, end=" ")

        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

def mirror(root):
    if root:
        root.left, root.right = root.right, root.left
        mirror(root.left)
        mirror(root.right)

def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left),
                   height(root.right))

def leaf_nodes(root):
    if root:
        if root.left is None and root.right is None:
            print(root.data, end=" ")

        leaf_nodes(root.left)
        leaf_nodes(root.right)

root = None

n = int(input("Enter number of nodes: "))

for i in range(n):
    data = int(input("Enter value: "))
    root = insert(root, data)

print("Original BST:")
level_order(root)

print("\nHeight:", height(root))

print("Leaf Nodes:")
leaf_nodes(root)

mirror(root)

print("\n\nNew Mirror Tree:")
level_order(root)
