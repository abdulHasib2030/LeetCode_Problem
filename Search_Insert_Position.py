class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] < target:
                k = i+1
            if nums[i] == target:
                return i

        return k
        