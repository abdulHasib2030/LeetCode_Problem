class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        import sys
        i, j, n, minn, summ = 0,0,len(nums), sys.maxsize, 0
        flag = False
        while j < n:
            summ += nums[j]
            
            while summ >= target:
                minn = min(minn, j -i+1)
                summ -= nums[i]
                flag = True
                i+= 1
            j+= 1
        if flag:
            return minn
        return 0