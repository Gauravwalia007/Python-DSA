class Node():
    def __init__(self,value):
        self.value=value
        self.next = None
        self.prev = None
        
class DoublyLinkedList():
    
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
    
    def pop(self):
        if self.head is None:
            return None
        temp = self.tail
        if self.length==1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length-=1
        return temp
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length+=1
        return True
    
    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        if self.length ==1:
            self.head=None
            self.tail=None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -=1
        return temp
    
    def get(self,index):
        if index < 0 or index >= self.length :
            return None
        if index < (self.length/2) :
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1,index,-1):
                temp = temp.prev
        return temp
    
    def set_value(self,index,value):
        tar = self.get(index)
        if tar:
            tar.value=value
            return True
        return False
    
    def insert(self,index,value):
        
        if index < 0 or index > self.length:
            return False
        if index == 0 :
            return self.prepend(value)
        if index == self.length:
            
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index)
        new_node.prev = temp.prev
        temp.prev.next = new_node
        temp.prev = new_node
        new_node.next = temp
        self.length+=1
        return True
    
    # def insert(self, index, value):
    #     if index < 0 or index > self.length:
    #         return False
    #     if index == 0:
    #         return self.prepend(value)
    #     if index == self.length:
    #         return self.append(value)

    #     new_node = Node(value)
    #     before = self.get(index - 1)
    #     after = before.next

    #     new_node.prev = before
    #     new_node.next = after
    #     before.next = new_node
    #     after.prev = new_node
        
    #     self.length += 1   
    #     return True 

    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0 :
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
    
    # Question 1 :-  Swap First and Last
    def swap_first_last(self):
        if self.head is None:
            return None
        temp = self.head.value
        self.head.value = self.tail.value
        self.tail.value = temp
        return True
    
    # Question 2 :- Reverse the DLL
    def reverse(self):
        if self.head is None:
            return False
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            temp.prev = after
            before = temp
            temp = after
    
    # Question 3 :- DLL: Palindrome Checker
    def is_palindrome(self):
        temp1 = self.head
        temp2 = self.tail
        counter = self.length//2
        for _ in range(counter):
            if temp1.value == temp2.value :
                temp1 = temp1.next
                temp2 = temp2.prev
            else:
                return False
        return True
    
    # Question 4 :- 
    def swap(self,n1,n2):
        # print(n1.prev,n1.value,n1.next, "||", n2.prev,n2.value,n2.next)
        n2.prev = n1.prev
        n1.next = n2.next
        n1.prev = n2
        n2.next = n1 
        if n1.next is not None:
            n1.next.prev = n1
        if n2.prev is not None:
            n2.prev.next = n2
        # print(n1.prev,n1.value,n1.next, "||", n2.prev,n2.value,n2.next)
    
    def swap_pairs(self):
        if self.length is None or self.length <= 1 :
            return None
        temp = self.head
        after = temp.next
        self.head = after
        counter = self.length//2
        for _ in range(counter):
            after = temp.next
            # print(temp.value,'----',after.value)
            self.swap(temp,after)
            # print(temp.value,'----',after.value)
            temp = temp.next
            # print(temp.value,'----',after.value)
            
if __name__ == "__main__":
    my_dll = DoublyLinkedList(1)
    my_dll.append(2)
    my_dll.append(3)
    my_dll.append(4)

    print('my_dll before swap_pairs:')
    my_dll.print_list()

    my_dll.swap_pairs() 


    print('my_dll after swap_pairs:')
    my_dll.print_list()


    """
        EXPECTED OUTPUT:
        ----------------
        my_dll before swap_pairs:
        1 <-> 2 <-> 3 <-> 4
        ------------------------
        my_dll after swap_pairs:
        2 <-> 1 <-> 4 <-> 3

    """