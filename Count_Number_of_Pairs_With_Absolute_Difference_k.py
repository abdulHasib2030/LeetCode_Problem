class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        cnt = 0
        dic = {}

        for i in range(len(nums)):
          if nums[i] not in dic.keys():
            dic[nums[i]] = 1
          else:
            dic[nums[i]] +=1
            
        for i in dic.keys():
          if i+k in dic.keys():
            cnt += dic[i] * dic[i+k]
            
        return (cnt)


        ## Brute Force
        # cnt = 0
        # for i in range(len(nums)):
        #   for j in range(i, len(nums)):
        #     if abs(nums[i]- nums[j]) == k:
        #       cnt+= 1
        # return cnt

        