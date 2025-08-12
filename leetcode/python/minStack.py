#August 12 2025
#Min Stack
#Notes: Thought of implementing it wihtout using any libraries, but apparently i can use pop for lists too.
#Notes: FOr initialising i thought of doing list=[], but then learnt about how self works. 

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

        

    def top(self) -> int:
        return self.stack[-1]       

    def getMin(self) -> int:
        return self.minStack[-1] 

            
        
