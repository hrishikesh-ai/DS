class Node:
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.left = None
        self.right = None
    
    def getInfo(self):
        print(f"Parent: {self.parent.data if self.parent else None}, Data: {self.data}, Left: {self.left.data if self.left else None}, Right: {self.right.data if self.right else None}")

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
    
    def insert(self, data: int):
        ptr = self.root
        newNode = Node(data)
        while ptr != None:
            if int(ptr.data) < data:
                if ptr.right:
                    ptr = ptr.right
                else:
                    newNode.parent = ptr
                    ptr.right = newNode
                    break

            elif int(ptr.data) > data:
                if ptr.left:
                    ptr = ptr.left
                else:
                    newNode.parent = ptr
                    ptr.left = newNode
                    break
    
    def delete_root(self):
        curPtr = self.root.right
        print(curPtr.data)
        if curPtr.left:
            while curPtr.left is not None:
                print(curPtr.data)
                if curPtr.left == None:
                    curPtr.parent = None
                    curPtr.left = self.root.left
                    self.root.left.parent = curPtr
                    self.root = curPtr
                    print("Did something")
                    return
                else:
                    curPtr = curPtr.left
        else:
            curPtr.parent = None
            curPtr.left = self.root.left
            self.root.left.parent = curPtr
            self.root = curPtr
    
    def delete_node(self, node: Node):
        curPtr = node
        if curPtr.left:
            while curPtr.left is not None:
                print(curPtr.data)
                if curPtr.left == None:
                    # curPtr.parent = None
                    # curPtr.left = self.root.left
                    # self.root.left.parent = curPtr
                    curPtr.parent = node.parent
                    node = curPtr
                    # curPtr.right = node.right
                    print("Did something")
                    return
                else:
                    curPtr = curPtr.left
        else:
            curPtr.parent = None
            curPtr.left = self.root.left
            self.root.left.parent = curPtr
            self.root = curPtr
                
    def delete(self, data: int):
        ptr = self.root
        while ptr != None:
            if int(ptr.data) == data:
                if ptr.left and ptr.right:
                    print("There are Two child nodes")
                    if self.root.data == data:
                        self.delete_root()
                    else:
                        self.delete_node(ptr)
                    return
                else:
                    if ptr.right and not ptr.left:
                        ptr.parent.right = ptr.right
                        print(f"{ptr.data} is deleted")
                        return
                    elif ptr.left and not ptr.right:
                        ptr.parent.left = ptr.left
                        print(f"{ptr.data} is deleted")
                        return
                return
            else:
                if int(ptr.data) < data:
                    if ptr.right:
                        ptr = ptr.right
                    else:
                        pass
                elif int(ptr.data) > data:
                    if ptr.left:
                        ptr = ptr.left
                    else:
                        pass
    
    def preorderTraversal(self, node: Node):
        if node:
            node.getInfo()
            self.preorderTraversal(node.left)
            self.preorderTraversal(node.right)
            
    def inorderTraversal(self, node: Node):
        if node:
            self.inorderTraversal(node.left)
            node.getInfo()
            self.inorderTraversal(node.right)

    def postorderTraversal(self, node: Node):
        if node:
            self.postorderTraversal(node.left)
            self.postorderTraversal(node.right)
            node.getInfo()

data = [10,5,20,3,6,15,21,13,35,33,40,37]

t1 = BinaryTree(26)

for i in data:
    t1.insert(i)

t1.delete(35)
t1.preorderTraversal(t1.root)
