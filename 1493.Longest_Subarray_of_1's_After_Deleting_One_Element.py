class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i, j, mx, cnt, ans , n = 0,0,0,0,0,len(nums)
        while j < n:
            if nums[j] == 0:
                cnt += 1
                while cnt > 1:
                    if nums[i] == 0:
                        cnt -= 1
                    else:
                        ans -= 1
                    i += 1
            else:
                ans +=1
                mx = max(mx, ans)
            j+=1
        if mx == n:
            return mx -1
        
        return mx
        