class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SLL:
    def __init__(self):
        self.head = None
    def reverse(self):
        prev = None
        curr = self.head
        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
        a = self.head                                                                                                                                                                                                                                                                                                      
        while a is not None:
            print(a.data, end = " ")
            a = a.next
        
        


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


sll.reverse()
