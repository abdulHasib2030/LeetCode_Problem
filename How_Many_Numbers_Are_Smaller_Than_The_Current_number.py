class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        ## Efficent Way 
        dic = {}
        ans = []
        sort_nums = sorted(nums)
        for i in range(len(sort_nums)):
            if sort_nums[i] not in dic:
                dic[sort_nums[i]] = i
        for i in nums:
            ans.append(dic[i])
        return ans
 


        ### brute Force 
        # ans = []
        # for i in range(len(nums)):
        #     cnt  = 0
        #     for j in range(len(nums)):
        #         if nums[i] > nums[j]:
        #             cnt +=1
        #     ans.append(cnt)
        
        # return ans
        