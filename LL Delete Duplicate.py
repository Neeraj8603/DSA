class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    def removeDuplicates(self):
        if self.head is None:
            return
        seen = set()
        current = self.head
        prev = None
        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next

    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

# Input handling
n1 = int(input())
if n1 == 0:
    print("List is empty")
else:
    list1 = list(map(int, input().split()))
    ll = LinkedList()
    for i in list1:
        ll.insertEnd(i)

    ll.removeDuplicates()
    ll.display()
