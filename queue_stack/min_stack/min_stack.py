
class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []
    def push(self, value: int) -> bool:
        self.stack.append(value)
        # If no value in mins or if the last min is bigger than the new value => append value to the mins
        if not self.mins or self.mins[-1] > value:
            self.mins.append(value)
        # Else => append the last value in mins to mins
        else:
            self.mins.append(self.mins[-1])
    def pop(self) -> int:
        if not self.stack: return None
        self.stack.pop()
        self.mins.pop()
    def top(self) -> int:
        if not self.stack: return None
        return self.stack[-1]
    def getMin(self) -> int:
        if not self.mins: return None
        return self.mins[-1]
    def __str__(self):
        return f"""
        Stack {self.stack} 
        Mins {self.mins}
        """
        
if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    print(minStack)
    minStack.push(0)
    print(minStack)
    minStack.push(-3)
    print(minStack)
    print("Get min: ", minStack.getMin()) # return -3
    minStack.pop()
    print(minStack)
    print("TOP: ", minStack.top()) # return 0
    print("MIN: ", minStack.getMin()) # return -2
    
    
    
    