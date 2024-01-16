class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i , j = 1, n-1
        import sys
        minn = 0
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            start = i+1
            end = n-1
            while start < end:
                summ = nums[i] + nums[start] + nums[end]
                if summ == target:
                    return (summ)
                if abs(summ - target) < abs(ans-target):
                    ans = summ
                if summ < target:
                    start +=1
                elif summ> target:
                    end -=1
                
                
        return ans

                