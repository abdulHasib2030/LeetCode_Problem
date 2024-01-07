import sys
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, j, mx, summ = 0,0, -sys.maxsize, 0
        n = len(nums)
        while n > j:
            summ += nums[j]
            if j < k-1:
                j+=1
            else:
                mx = max(mx, summ)
                summ -= nums[i]
                i+=1
                j += 1
        return mx / k
        