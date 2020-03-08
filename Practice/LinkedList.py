# Base node class
class Node:
    def __init__(self,data):
        self.data = data #Current nodes data
        self.next = None # [data][NULL]
    
class LinkedList:
    def __init__(self):
        self.head = None # Initializing Linked list

    def insert(self, new_data): 
 
        if(self.head == None): 
            self.head = Node(new_data)
            return
        
        last = self.head           # need to have a temporary node to traverse 
        while (last.next != None): # because if we traverse with self.head 
            last = last.next       # then run our printall function, we would be
                                   # already traversing the list thus changing
        last.next =  Node(new_data)# self.head which makes our printall func 
                                   # useless  
    def printall(self):
        while(self.head != None):
            print(self.head.data)
            self.head = self.head.next

lists = LinkedList()
lists.head = Node(1)
second = Node(2)
third = Node(3)
lists.head.next = second
second.next = third

lists.insert(5)
lists.insert(6)
lists.insert(7)

lists.printall()
