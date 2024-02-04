class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        lst = []
        for i in range(n):
            lst.append(start+2*i)
        ans = 0
        for i in lst:
            ans ^=i
        return (ans)