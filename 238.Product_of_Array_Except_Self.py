class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []
        import math

        zero = nums.count(0)
        if zero > 1:
            lst = [0 for i in range(len(nums))]
            return (lst)
        else:  
            if zero == 0:
                mul = math.prod(nums)
                for i in nums:
                    lst.append(mul//i)
            else:
                mul = 1
                for i in nums:
                    if i != 0:
                        mul *= i 
                for i in nums:
                    if i == 0:
                        lst.append(mul)
                    else:
                        lst.append(0)
            
            return (lst)
