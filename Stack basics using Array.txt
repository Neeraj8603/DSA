class Stack:
    def __init__(self):
        self.arr = [0] * 100
        self.top = -1

    def push(self, data):
        if self.top < 100:
            self.top += 1
            self.arr[self.top] = data
        else:
            print("Stack Overflow")

    def pop(self):
        if self.top >= 0:
            self.top -= 1
        else:
            print("Stack Underflow")

    def size(self):
        print(self.top + 1)

    def top1(self):
        if self.top >= 0:
            print(self.arr[self.top])
        else:
            print("Stack is empty")

    def isEmpty(self):
        if(self.top == -1):
            print('true')
        else:
            print('false')


N = int(input())
s = Stack()
for _ in range(N):
    c = input().strip().split()
    if c[0] == "Push":
        data = c[1]
        s.push(data)
    elif c[0] == "Pop":
        s.pop()
    elif c[0] == "Size":
        s.size()
    elif c[0] == "Top":
        s.top1()
    elif c[0] == "IsEmpty":
        s.isEmpty()
