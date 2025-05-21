class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_begin(self, node):
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node
    
    def insert_end(self, node):
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
       

    def insert_at(self, pos, node):
        a = self.head
        for i in range(pos-1):
            a = a.next
        node.next = a.next
        a.next.prev = node
        a.next = node
        node.prev = a
        

    def delete_begin(self):
        a = self.head 
        self.head = a.next
        self.head.prev = None

    def delete_end(self):
        self.tail  = self.tail.prev
        self.tail.next = None

    def delete_at(self, pos):
        a = self.head
        for i in range(pos-1):
            a = a.next
        a.next = a.next.next
        a.next.prev = a

    def traverse_forward(self):
        a = self.head
        while a is not None:
            print(a.data, end=" ")
            a = a.next
        print("\n")
    
    def reverse(self):
        a = self.tail
        while a is not None:
            print(a.data, end=" ")
            a = a.prev
        print("\n")


    
n1 = Node(1)
n2 = Node(2)
n1.prev = None
n1.next = n2 
n3 = Node(3)
n2.prev = n1
n2.next = n3
n4 = Node(4)
n3.prev = n2
n3.next = n4
n5 = Node(5)
n4.prev = n3
n4.next = n5
n5.prev = n4
dll = DLL()
dll.head = n1
dll.tail = n5
dll.traverse_forward()

n0 = Node(0)
dll.insert_begin(n0)
dll.traverse_forward()

n6 = Node(6)
dll.insert_end(n6)
dll.traverse_forward()

n7 = Node(7)
dll.insert_at(3, n7)
dll.traverse_forward()

dll.delete_begin()
dll.traverse_forward()

dll.delete_end()
dll.traverse_forward()

dll.delete_at(3)
dll.traverse_forward()