class Stacks:

    def __init__(self):
        self._stack=[]
        self._length=0

    
    def push(self,value):
        self._stack.append(value)
        self._length+=1


    def pop(self):
        self._length-=1
        return self._stack.pop()

    def peek(self):
        if(self._stack):
            return self._stack[-1]
        else:
            return([])
    
    def isEmpty(self):
        return False if(self._stack) else True
    
    def __str__(self):
        return("<"+str(self._stack[:])+">")

    def height(self):
        return(self._length)


if __name__=="__main__":
    S1=Stacks()
    print(S1.isEmpty())
    print(S1.peek())
    S1.push(1)
    print(S1.height())
    print(S1.isEmpty())
    S1.push(4)
    print(S1.height())
    print(S1.peek())
    print(S1)
    print(S1.pop())
    print(S1.peek())
    print(S1.height())
    print(S1)





        