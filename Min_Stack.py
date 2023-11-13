class MinStack:

    def __init__(self):
        self.lst = []

    def push(self, val: int) -> None:
        self.lst.append(val)

    def pop(self) -> None:
        self.lst.pop()
        

    def top(self) -> int:
        return self.lst[-1]
        

    def getMin(self) -> int:
        return min(self.lst)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()