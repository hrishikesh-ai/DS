class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
        self.prevAddress = None

    def getInfo(self):
        print("Node details: " + str(self.data) + " Next: " + str(self.next))
    
class NodeList:
    def __init__(self):
        self.start = None 
        self.last = None 
    
    def appendlast(self, data):
        newNode = Node(data)

        if self.start == None:
            self.start = newNode
            self.last = newNode
        
        else:
            self.last.next = newNode
            self.last = newNode

    def appendFirst(self,data):
        newNode = Node(data)
        newNode.next = self.start
        self.start = newNode

    def traverse(self):
        if self.start == None:
            print("Your list is empty")
        else:
            ptr = self.start
            while ptr != None:
                print(ptr)
                ptr.getInfo()
                ptr = ptr.next
    
    def peek(self):
        print(self.last.data)

    def delete_last(self):
        if self.start == None:
            print("List is Empty")
        else:
            ptr = self.start
            while ptr.next.next != None:
                ptr = ptr.next
            ptr.next = None
    
    def delete_first(self):
        if self.start ==None:
            print("The list is Empty")
        else:
            self.start  = self.start.next

    def delete_pos(self, pos):
        # prevAddress = None
        print('')
        if self.start == None:
            print("List is Empty")
        else:
            counter = 0
            ptr = self.start
            nextAddress = None

            for i in range(pos):
                if counter <= pos:
                    self.prevAddress = ptr
                    ptr = ptr.next
                    # print(self.prevAddress)
                    # print(counter)
                    nextAddress = ptr.next
                    
                    counter += 1

                elif counter == pos:
                    # self.prevAddress.next = 
                    # print(nextAddress)
                    # print(self.prevAddress)
                    # ptr.getInfo()
                    # new_ptr = self.start
                    new_counter = 0
                    curr_value = None
                    while new_counter < counter:
                        # if new_ptr.next == self.prevAddress:
                        #     new_ptr.next = nextAddress
                        # new_ptr = new_ptr.next
                        # print(new_counter)
                        curr_value = self.start.next
                        print(curr_value.getInfo())
                        new_counter += 1
                    curr_value = self.prevAddress
                    curr_value.next = nextAddress
                
a = 4
i = 1
list = NodeList()
# list.appendlast
while i<= a:
    c = int(input('enter the data : '))
    list.appendlast(c)
    i += 1

list.traverse()

# list.peek()
# list.delete_last()

# list.traverse()

# list.delete_first()

# list.traverse()

list.delete_pos(2)
# list.traverse()