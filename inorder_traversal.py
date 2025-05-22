class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def Inorder(node):
    if node is None:
        return
    else:
        Inorder(node.left)
        print(node.data, end=" ")
        Inorder(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print(Inorder(root))