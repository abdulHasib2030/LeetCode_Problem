class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        i, j = 0,1
        for k in nums:
            if k > 0:
                ans[i] = k
                i+=2
            else:
                ans[j] = k
                j+=2
        return ans


    
        