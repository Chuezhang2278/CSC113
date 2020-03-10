class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
        
def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.val),
        inOrder(root.right)

def BFS(root):


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)

inOrder(root) 
