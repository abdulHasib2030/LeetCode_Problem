class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    
        i, j, n = 0,0,len(nums)
        lst = []
        ans = []
        while j < n:
            while len(lst) > 0 and lst[len(lst)-1] < nums[j]:
                lst.pop(len(lst)-1)
            lst.append(nums[j])
            if j < k-1:
                j+=1
            else: 
                ans.append(lst[0])
                if nums[i] == lst[0]:
                    lst.pop(0)
                j+=1
                i += 1
        return (ans)

        