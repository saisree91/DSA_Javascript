class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SLL:
    def __init__(self):
        self.head = None
    def reverse(self, head):
        prev = None
        curr = head
        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def traversal(self):
        a = self.head
        while a is not None:
            print(a.data, end = " ")
            a = a.next
        print("\n")

    def palindrome(self):
        slow = self.head
        fast = self.head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        newhead = self.reverse(slow.next)
        first = self.head
        second = newhead
        while(second is not None):
            if first.data != second.data:
                self.reverse(newhead)
                return False
            else:
                first = first.next
                second = second.next
        self.reverse(newhead)
        return True

n1 = Node(int(input("enter node: ")))
n2 = Node(int(input("enter node: ")))
n1.next = n2
n3 = Node(int(input("enter node: ")))
n2.next = n3
n4 = Node(int(input("enter node: ")))
n3.next = n4
n5 = Node(int(input("enter node: ")))
n4.next = n5
sll = SLL()
sll.head = n1


print(sll.palindrome())
sll.traversal()