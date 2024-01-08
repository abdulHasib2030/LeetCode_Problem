class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lst = {}
        for i , num in enumerate(nums):
            if num in lst and i - lst[num] <= k:
                return True
            lst[num] = i

        return False