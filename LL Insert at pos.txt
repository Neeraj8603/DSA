class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, id):
        new_node = Node(id)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def posi(self, id, pos):
        new_node = Node(id)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 1
        while current and count < pos-1:
            current = current.next
            count += 1
      # print(current.data)

        new_node.next = current.next
        current.next = new_node

    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

N = int(input())
ids = list(map(int, input().split()))
pos = int(input())
p = int(input())
list1 = LinkedList()
for id in ids:
    list1.insert(id)

list1.posi(p, pos)
list1.display()
