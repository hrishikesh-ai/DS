class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getInfo(self):
        print(f"The Node data is {self.data} and the next is {self.next}")

class MyQueue:
    def __init__(self):
        self.top = None
        self.last = None
    
    def enqueue(self,data):
        newNode = Node(data)
        if self.top == None:
            self.top = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
    
    def traverse(self):
        if self.top == None:
            print("Queue is Empty")
        else:
            ptr = self.top
            while ptr != None:
                ptr.getInfo()
                ptr = ptr.next

    def dequeue(self):
        if self.top == None:
            print("Queue is Empty")
        else:
            de_q_el = self.top.data
            self.top = self.top.next
            print(f"Dequeue Element: {de_q_el}")

q1 = MyQueue()
a = int(input("Enter the no. of Nodes: "))

for i in range(a):
    dt = input("Enter the Node Details: ")
    q1.enqueue(dt)

q1.traverse()
q1.dequeue()
q1.traverse()