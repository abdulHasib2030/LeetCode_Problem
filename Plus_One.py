class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st = ""
        for i in digits:
          st+= str(i)
        st = int(st)+1
        lst = []
        while st > 0:
          lst.append(st%10)
          st = st // 10
        
        lst.reverse()
        return(lst)
            
                