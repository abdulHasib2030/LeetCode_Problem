import sys
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j, n = 0,0,len(nums)
        minn = sys.maxsize
        for i in range(k-1, n):
            res = nums[i] - nums[i-k+1]
            minn = min(minn, res)
        return minn

       


        