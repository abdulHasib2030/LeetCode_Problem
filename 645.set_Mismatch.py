class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                ans.append(nums[i])
        
        for i in range(1, len(nums)+1):
            if i not in nums:
                ans.append(i)
        
        
        return ans
        