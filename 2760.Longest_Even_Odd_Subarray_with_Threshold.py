
class Solution:
    def longestAlternatingSubarray(
        self, nums: List[int], threshold: int
    ) -> int:
        mx= 0
        n = len(nums)

        for i in range(n):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                mx = max(mx, 1)

                for j in range(i+1, n):
                    if nums[j] % 2 == nums[j-1] % 2:
                        break
                    if nums[j] > threshold:
                        break
                    mx = max(mx, j - i +1)

        return mx

