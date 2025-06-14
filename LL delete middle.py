# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
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
    def delete(self,n1):
        if (n1%2==0):
            n1=(n1/2)+1
        else:
            n1=math.ceil(n1/2)
        count = 0
        while self.head and count<n1-1:
            count = count + 1
            self.head = self.head.next   
            
    def display(self):
        current = self.head
        while current:
            print(current.data,end=" ")
            current = current.next
        
n1 = int(input()) 
list1 = list(map(int,input().split()))
ll = LinkedList()
for i in list1:
    ll.insertEnd(i)    
    
ll.delete(n1)
ll.display()
