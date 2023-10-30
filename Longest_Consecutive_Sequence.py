class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        if len(nums) == 0:
            return 0
        cnt  = 1
        maxi = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    cnt += 1
                else:
                    maxi = max(maxi, cnt)
                    cnt = 1

        return ( max(maxi, cnt))



        