class Solution:
    def maxSubArray(self, nums) -> int:
        ### This is Brute Force Approach 
        # maxSum = -10**4 
        # maxEnd = 0
        # for i in nums:
        #     maxEnd = max(i, maxEnd + i)
        #     maxSum = max(maxSum, maxEnd)
        # return maxSum

        ### This is Kadane's Algorithm
        ## explain kadane's algorithm
        currentSum = 0
        maxSum = -10**4 
        for i in nums:
            currentSum += i
            if currentSum > maxSum:
                maxSum = currentSum
            if currentSum < 0:
                currentSum = 0
        return maxSum      


ans = Solution()
nums =  [5,4,-1,7,8]
print(ans.maxSubArray(nums))