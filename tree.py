class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
 

root = TreeNode(1)
L1N1 = TreeNode(2)
L1N2 = TreeNode(3)
root.add_child(L1N1)
root.add_child(L1N2)
L1N1.add_child(TreeNode(4))
L1N1.add_child(TreeNode(5))
L1N1.add_child(TreeNode(6))
L1N2.add_child(TreeNode(7))
L1N2.add_child(TreeNode(8))
L1N2.add_child(TreeNode(9))
