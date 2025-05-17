class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SLL:
    def __init__(self):
        self.head = None
    def traversal(self):
        a = self.head
        while a is not None:
            print(a.data, end = " ")
            a = a.next
        print("\n")
    def insert_at_begin(self, node):
        node.next = self.head
        self.head = n0 
    def insert_at_end(self, node):
        b = self.head
        while b.next is not None:
            b = b.next
        b.next = node
        node.next = None
        

n1 = Node(1)
n2 = Node(2)
n1.next = n2
n3 = Node(3)
n2.next = n3
n4 = Node(4)
n3.next = n4
n5 = Node(5)
n4.next = n5
sll = SLL()
sll.head = n1
sll.traversal()

n0 = Node(0)
sll.insert_at_begin(n0)
sll.traversal()

n6 = Node(6)
sll.insert_at_end(n6)
sll.traversal()