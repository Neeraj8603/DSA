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

    def deletePos(self, pos):
        if pos <= 0:
            return
        if pos == 1:
            if self.head:
                self.head = self.head.next
            return
        current = self.head
        count = 1
        while current and count < pos - 1:
            current = current.next
            count += 1
        if current and current.next:
            current.next = current.next.next

    def display(self):
        current = self.head
        if not current:
            print("List is empty")
            return
        while current:
            print(current.data, end=" ")
            current = current.next

# Input handling
n1 = int(input())
if n1 == 0:
    print("List is empty")
else:
    list1 = list(map(int, input().split()))
    a = int(input())  # position to delete
    ll = LinkedList()
    for i in list1:
        ll.insertEnd(i)

    ll.deletePos(a)
    ll.display()
