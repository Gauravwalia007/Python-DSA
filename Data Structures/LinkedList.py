class Node():
    
    def __init__(self,value):
        self.value=value
        self.next=None
        
class LinkedList():
    
    def __init__(self,value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self):
        temp = self.head
        while(temp != None):
            print(temp.value,end="->")
            temp = temp.next
        print("None")
    
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.head is None:
            return None
        else:
            res = self.tail
            res.next = None
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                temp = self.head
                while temp.next is not res:
                    temp = temp.next
                self.tail = temp
            self.length -= 1
        return res

    def prepend(self,value):
        new_node=Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length+=1
        return True
    
    def pop_first(self):
        
        if self.head is None:
            return None
        else:
            res = self.head
            if self.length ==1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.length -= 1
        
        return res
    
    def get(self,index):
        if self.length == 0 or self.length <= index or index < 0:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp
    
    def set_value(self,index,value):
        if index < 0 or index >= self.length:
            return False
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value=value
        return True
    
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        res = self.get(index) 
        pre = self.get(index-1)
        
        pre.next = res.next
        res.next = None
        self.length-=1
        return res
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after=temp.next
            temp.next = before
            before = temp
            temp = after

    # Question 1 :- Find Middle Node (two-pointer approach)
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        if self.head == None:
            return None
        if fast.next == None :
            return slow
        while(fast):
            fast = fast.next
            if fast == None:
                break
            slow = slow.next
            fast = fast.next
        return slow
    
    # Question 2 :- To Find if the List has a loop in it 
    # (Floyd's cycle-finding algorithm (also known as the "tortoise and the hare" algorithm))
    def has_loop(self):
        slow = self.head
        fast = self.head
        if self.head == None:
            return False
        while(fast):
            fast = fast.next
            if fast == None:
                return False
            slow=slow.next 
            fast=fast.next
            if slow == fast:
                return True
        return False
    
    # Question 4 :- To rearrange the list based on a no such that all small values are on left and 
    # all qual and big values are on the right of this no. keeping the original sequence 
    def partition_list(self,x):
        if self.head == None:
            return None
        temp = self.head
        left = None
        right = None
        while temp is not None:
            if temp.value < x :
                if left == None:
                    left = LinkedList(temp.value)
                else:
                    left.append(temp.value)
            else:
                if right == None:
                    right = LinkedList(temp.value)
                else:
                    right.append(temp.value)
            temp = temp.next
        if left == None:
            self.head = right.head
        elif right == None:
            self.head = left.head
        else :
            curr = left.head
            while curr.next is not None:
                curr = curr.next
            curr.next = right.head
            self.head = left.head
        left = None
        right = None
    
    # Question 5 :- To remove the duplicate values from the LL
    def remove_duplicates(self):
        
        if self.head == None:
            return None
        pre_node = self.head
        curr_node = pre_node.next
        num = {pre_node.value}
        while(curr_node):
            if curr_node.value in num:
                pre_node.next = curr_node.next
                curr_node.next = None
                curr_node = pre_node.next
            else:
                num.add(curr_node.value)
                curr_node = curr_node.next
                pre_node = pre_node.next
    
    # Question 6 :- To Convert a binary no to decimal from LL
    def binary_to_decimal(self):
        x=self.length-1
        res=0
        
        temp = self.head
        
        for i in range(self.length):
            res += 2**x * temp.value
            x -= 1
            temp = temp.next
        
        return res
    
    # Question 7 :- To reverse the LL between two Index values

# Question 3 :- To Find Kth Node From End   
def find_kth_from_end(linked_list,k):
    slow = linked_list.head
    fast = linked_list.head
    
    # if k<=0:
    #     return None
        
    # if linked_list == None:
    #     return None
        
    for _ in range(k):
        if fast == None:
            return None
        fast = fast.next

    while(fast):
        slow = slow.next
        fast = fast.next
        
    return slow

if __name__=='__main__':
    myList = LinkedList(5)
    myList.append(2)
    myList.append(3)
    myList.append(4)
    myList.print_list()