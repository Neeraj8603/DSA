# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def end(self, id):
        new_node = Node(id)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def swap(self):
        current = self.head
        while current and current.next:
            temp = current.data
            current.data = current.next.data
            current.next.data = temp
            current = current.next.next
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        
N = int(input())
ids = list(map(int, input().split()))

list1 = LinkedList()
for id in ids:
    list1.end(id)

list1.swap()
list1.display()
