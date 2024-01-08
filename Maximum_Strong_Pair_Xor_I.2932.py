
# ## Bruate Force Apporch
import sys
# class Solution:
#     def maximumStrongPairXor(self, nums: List[int]) -> int:
#         mx = -sys.maxsize
#         n = len(nums)
#         for i in range(n):
#             for j in range(n):
#                 if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
#                     ans = nums[i] ^ nums[j]
#                 mx = max(ans, mx)
#         return mx 

# ## one Line Solution
# nums = [5,6,25,30]
# print(max(x ^ y for x in nums for y in nums if abs(x - y) <= min(x, y)))

# ##Optimize Soution: Time Complexity o(nlogn)

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        ans = 0
        for idx, value in enumerate(nums):
            mx = value * 2 
            for y in range(idx + 1, len(nums)):
                if nums[y] > mx:
                    break
                ans = max(ans, value^ nums[y])
        return ans

       