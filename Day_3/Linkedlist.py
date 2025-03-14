class Node:
    def __init__(self,data):
        self.data = data # stores data
        self.next = None # stores reference to next node/ pointer to next node

class linkedList:
    def __init__(self):
        self.head =None # stores reference to head node/ pointer to head node
        
    def insert(self,data):
        node1 = Node(data)
        if not self.head:
            self.head = node1
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node1
            
    def display(self):
        current = self.head
        while current:
            print(current.data,end="->")
            current = current.next
        print("None")

obj = linkedList()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.insert(40)
obj.insert(50)
obj.display()