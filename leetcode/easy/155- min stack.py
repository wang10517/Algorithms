class Entry(object):
    def __init__(self, value , prev):
        self.value = value 
        self.prev = prev
        if not prev is None:
            self.min = min(prev.min, self.value)
        else:
            self.min = self.value


class MinStack(object):
        
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append(Entry(x,None))
        else:
            self.stack.append(Entry(x,self.stack[-1]))
        return None

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
        return None
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1].value

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1].min
        
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
