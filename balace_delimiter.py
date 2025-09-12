class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def getInfo(self):
        print(f"The Node data is {self.data} and the next is {self.next}")

class BalanceDelimiter:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        newNode = Node(data)
        if self.top == None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
    
    def pop(self):
        if self.top == None:
            print("Stack is Empty")
        else:
            pop_el = self.top.data
            self.top = self.top.next
            return pop_el
    
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
    
    def peek(self):
        if self.top == None:
            print("The Stack is Empty")
            return False
        else:
            return self.top.data
    
    def traverse(self):
        if self.top == None:
            print("Stack is Empty")
        else:
            ptr = self.top
            while ptr != None:
                ptr.getInfo()
                ptr = ptr.next

def braceStack():
    deli = BalanceDelimiter()
    a = input('Enter the Equation: ')

    for i in a:
        if i in '{[(':
            deli.push(i)
        
        elif i in ')]}':
            peek_el = deli.peek()
            print(f"Peek Element is {peek_el}")
            pop_el = deli.pop()
            print(f"Pop Element is {pop_el}")
            print(i, peek_el, pop_el)

            # if peek_el != '(' and pop_el != ')' or peek_el != '[' and pop_el != ']' or peek_el != '{' and pop_el != '}':
            #     return False

            # if peek_el != pop_el:
            #     return False
    deli.traverse()
    return deli.isEmpty()

if braceStack():
    print("Equation is Balance Delimiter")
else:
    print("Equation is not Balance Delimiter")