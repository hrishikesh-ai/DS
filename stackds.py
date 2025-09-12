class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

    def getInfo(self):
        print("Node details: " + str(self.data), self.next)
    
class Stack:
    def __init__(self):
        self.start = None 
        self.last = None

    def traverse(self):
        if self.start == None:
            print("Your list is empty")
        else:
            ptr = self.start
            while ptr != None:
                print(ptr)
                ptr.getInfo()
                ptr = ptr.next
    def push(self,data):
        newNode = Node(data)
        if self.start == None:
            self.start = newNode
        else:
            newNode.next = self.start
            self.start = newNode
    
    def pop(self):
        if self.start == None:
            print("stack is empty")
        else:
            ptr = self.start
            print(ptr.data)
            ptr.next
            
a = 4
i = 1
list = Stack()
# list.appendlast
while i<= a:
    c = int(input('enter the data : '))
    list.push(c)
    i +=1

# list.traverse()
list.push(50)
# list.traverse()
list.pop()
list.traverse()

# list.push(10)
# list.traverse()
# list.peek()
# list.delete_last()

# list.traverse()

# list.delete_first()

# list.traverse()

# list.delete_pos(2)
# list.traverse()


            # while ptr != None:
            #     if ptr.next == self.last:
            #         de_q_el = self.last.data
            #         ptr = None
            #         print(f"Popped Element: {de_q_el}")
            #     if ptr.next == None:
            #         de_q_el = self.top.data
            #         self.top = None
            #         print(f"Popped Element: {de_q_el}")
            #     ptr = ptr.next