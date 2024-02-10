class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dic ={0:0}
        s = 0
        for i in range(n):
            s += nums[i]
            if s % k not in dic:
                dic[s%k] = i+1
            elif dic[s%k] < i:
                return True
        return False
