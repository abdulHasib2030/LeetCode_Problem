class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        i, j, n, cnt = 0,0,len(nums), 0
        presum = 0
        dic = {}
        dic[0] = 1
        for num in nums:
            presum += num
            if presum -k in dic:
                cnt += dic[presum-k]
            if presum not in dic:
                dic[presum] = 1
            else:
                dic[presum] = dic[presum]+1
        return (cnt)


