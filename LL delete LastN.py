# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            current = self.head
            while current.next :
                current = current.next
            current.next = newNode
    
    def deleteLastN(self, total, n):
        if n >= total:
            self.head = None
            return
        current = self.head
        count = 0
        while count < total - n - 1:
            current = current.next
            count += 1
        current.next = None
            
    def display(self):
        current = self.head
        if not current :
            print("List is empty")
            return
        while current :
            print(current.data,end=" ")
            current = current.next
            
n1 = int(input())
list1 = list(map(int, input().split()))
a = int(input())
ll = LinkedList()
for i in list1:
    ll.insertEnd(i)

ll.deleteLastN(n1,a)
ll.display()
