class Queue:
    def __init__(self):
        self.arr = []
        self.front = 0

    def enqueue(self, data):
        self.arr.append(data)

    def dequeue(self):
        if self.front == len(self.arr):
            print("Queue is empty.")
        else:
            print("Served Customer:", self.arr[self.front])
            self.front += 1

    def display(self):
        if self.front == len(self.arr):
            print("Queue is empty.")
        else:
            print("Current Queue:", ' '.join(self.arr[self.front:]))


n = int(input())
n1 = int(input())
q = Queue()
for _ in range(n1):
  c = input().strip().split()
  if c[0] == "ENQUEUE":
    q.enqueue(c[1])
  elif c[0] == "DEQUEUE":
    q.dequeue()
  elif c[0] == "DISPLAY":
    q.display()
