class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def start(self, task_id):
        new_node = Node(id)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

N = int(input())
ids = list(map(int, input().split()))

list1 = LinkedList()
for id in ids:
    list1.start(id)
    
list1.display()
