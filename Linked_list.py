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
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = node
        node.next = None
    def insert_at_specific(self, k, node):
        a = self.head
        for i in range(k-1):
            a = a.next
        node.next = a.next
        a.next = node
    def delete_begin(self):
        a = self.head
        self.head = a.next
        a.next = None
    def delete_end(self):
        a = self.head
        while a.next.next is not None:
            a = a.next
        a.next = None
    def delete_at(self, k):
        a = self.head
        for i in range(k-1):
            a = a.next
        a.next = a.next.next
    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True
        return False
        
        
        

n1 = Node(1)
n2 = Node(2)
n1.next = n2
n3 = Node(3)
n2.next = n3
n4 = Node(4)
n3.next = n4
n5 = Node(5)
n4.next = n5
n5.next = n3
sll = SLL()
sll.head = n1
# sll.traversal()

# n0 = Node(0)
# sll.insert_at_begin(n0)
# sll.traversal()

# n6 = Node(6)
# sll.insert_at_end(n6)
# sll.traversal()

# n7 = Node(7)
# sll.insert_at_specific(3, n7)
# sll.traversal()

# sll.delete_begin()
# sll.traversal()

# sll.delete_end()
# sll.traversal()

# sll.delete_at(4)
# sll.traversal()

print(sll.detect_cycle())