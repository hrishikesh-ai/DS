class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
    
    def getInfo(self):
        print(f"prev: {self.prev}, data: {self.data}, next: {self.next}")

class DoublyLinkedList:
    def __init__(self):
        self.start = None
        self.last = None
    
    def appendLast(self, data):
        newNode = Node(data)
        if self.start == None:
            self.start = newNode
            self.last = newNode
        else:
            newNode.prev = self.last
            self.last.next = newNode
            self.last = newNode
    
    def traverse(self):
        if self.start == None:
            print("LinkedList is Empty")
        else:
            ptr = self.start
            while ptr != None:
                ptr.getInfo()
                ptr = ptr.next

    def traverseBack(self):
        if self.start == None:
            print("LinkedList is Empty")
        else:
            ptr = self.last
            while ptr != None:
                ptr.getInfo()
                ptr = ptr.prev

    def appendFirst(self, data):
        newNode = Node(data)
        if self.start == None:
            self.start = newNode
            self.last = newNode
        else:
            self.start.prev = newNode
            newNode.next = self.start
            self.start = newNode
    
    def appendPos(self, data, pos):
        newNode = Node(data)
        if self.start == None:
            print("LinkedList is Empty")
        else:
            counter = 1
            ptr = self.start
            while ptr != None:
                if counter == pos:
                    # print("Got the Address", counter)
                    print(ptr.data)
                    newNode.prev = ptr.prev
                    newNode.next = ptr.next
                    ptr.next = newNode
                    break
                # print(counter)
                counter += 1
                ptr = ptr.next
    
    def deleteLast(self):
        if self.start == None:
            print("LinkedList is Empty")
        else:
            # prev_add = self.last.prev
            self.last = self.last.prev
            self.last.next = None
    
    def deletePos(self, pos):
        if self.start == None:
            print("LinkedList is Empty")
        else:
            counter = 1
            ptr = self.start
            while ptr != None:
                if counter == (pos + 1):
                    print(ptr.prev.data, ptr.data, ptr.next.data)
                    ptr.prev.next = ptr.next
                    break
                counter += 1
                ptr = ptr.next

    def deleteFirst(self):
        if self.start == None:
            print("LinkedList is Empty")
        else:
            self.start = self.start.next
            self.start.prev = None

l1 = DoublyLinkedList()

a = int(input("Enter the no. of Nodes: "))

for i in range(a):
    dt = input("Enter the data: ")
    l1.appendLast(dt)

l1.appendFirst(50)
l1.traverse()
print()
l1.appendPos(90, 2)
print()
l1.traverse()
print()
l1.traverseBack()
# l1.deletePos(2)
# l1.deleteFirst()
# l1.traverse()
# l1.traverseBack()
# 30/06
# 11/07
# 