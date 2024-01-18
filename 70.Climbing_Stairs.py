class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0,1
        if n == 1:
            return n
        for i in range(n):
            a, b = b, a+b
        return b
        
       
        # if n == 1:
        #     return n
        # dp = [0]*(n+1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n] 