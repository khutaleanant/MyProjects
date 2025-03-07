class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def insert(self,data):
    #compare the new value with the parent node
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left =Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right =Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert ,ethod to add nodes
root=Node(12)
root.insert(10)
root.insert(3)
root.insert(30)
root.PrintTree()
root.insert(7)
root.PrintTree()