class queue:
    
    def __init__(self):
        self._entries=[]
        self._length=0
    

    def put(self,value):
        self._entries.append(value)
        self._length+=1

    
    def get(self):
        self._length-=1
        return self._entries.pop(0)
    
    def __str__(self):
        printed="<"+str(self._entries[:])+">"
        return printed
    
    def get_length(self):
        return self._length

if __name__ =="__main__":

    Q1=queue()
    Q1.put(2)
    Q1.put(5)
    Q1.put(8)
    print(Q1)
    print(Q1.get_length())
    print(Q1.get())
    print(Q1)
    print(Q1.get_length())
    print(Q1.get())
    print(Q1)
    print(Q1.get_length())

