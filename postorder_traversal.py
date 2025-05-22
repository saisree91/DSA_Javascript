class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def Postorder(node):
    if node is None:
        return
    else:
        Postorder(node.left)
        Postorder(node.right)
        print(node.data, end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print(Postorder(root))