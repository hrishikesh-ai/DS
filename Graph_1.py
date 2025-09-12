class Node:
    def __init__(self, data):
        self.data = data

class GraphImp:
    def __init__(self):
        self.nodelist = []
        self.matrix = []

    def addNode(self):
        n = int(input("Enter no of Nodes: "))
        for i in range(0, n):
            self.matrix.append([])
            for j in range(0, n):
                self.matrix[i].append(0)
            node = input("Enter a Node: ")
            graph = Node(node)
            self.nodelist.append(graph)
    
    def addEdge(self, edge):
        row = -1
        column = -1
        for i in range(len(self.nodelist)):
            if self.nodelist[i].data == edge[0]:
                row = i
            if self.nodelist[i].data == edge[1]:
                column = i
            
        if row == -1 or column == -1:
            print("Invalid Edge. PLease break your edging streak")
        else:
            weight = int(input("Enter the Weight: "))
            self.matrix[row][column] = weight
    
    def printGraph(self):
        for i in range(len(self.nodelist)):
            # print(i.data)
            print(self.matrix[i])
        
g1 = GraphImp()
g1.addNode()

print()
print(g1.matrix)

edgeNo = int(input("Enter no of Edges: "))
for i in range(edgeNo):
    edge = input("Enter Edge: ")
    g1.addEdge(edge)
g1.printGraph()