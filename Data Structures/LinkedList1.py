class Node():

    def __init__(self,value):
        self.data = value
        self.next = None
    

class LinkedList():

    def __init__(self):
        self._head = None

    def head(self,Node):
        self._head=Node
    
    def printList(self):
        self.temp=self._head
        while(self.temp):
            print(self.temp.data,end=" -> ") if self.temp.next else print(self.temp.data)
            self.temp=self.temp.next

    def append_head(self,Node):
        Node.next=self._head
        self.head(Node)
    
    def append_tail(self,Node):
        self.temp=self._head
        while(self.temp):
            if (self.temp.next==None):
                self.temp.next=Node
                break
            self.temp=self.temp.next

    def remove(self):
        pass


if __name__=='__main__':
    L1= LinkedList()
    n1=Node(4)
    n2=Node(2)
    n3=Node(6)
    L1.head(n1)
    n1.next=n2
    n2.next=n3
    L1.printList()
    n4=Node(8)
    L1.append_head(n4)
    L1.printList()
    n5=Node(10)
    L1.append_tail(n5)
    L1.printList()

        
