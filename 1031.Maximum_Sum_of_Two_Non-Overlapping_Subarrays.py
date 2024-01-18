class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def solve(nums, p,  q):
            k = p
            sum1 = 0
            mx , total = 0,0
            i, j =0,0
            n = len(nums)
            while j < n:
                sum1 += nums[j]
                if j - i + 1 < k:
                    j += 1
                else:
                    smax = 0
                    sum2 = 0
                    x , y = j + 1, j +1
                    while y < n:
                        sum2 += nums[y]
                        if (y - x + 1 < q):
                            y += 1
                        else:
                            smax  = max(smax, sum2)
                            sum2 -= nums[x]
                            x += 1
                            y += 1
                    mx = max(mx, smax + sum1)
                    sum1 -= nums[i]
                    i+=1
                    j+= 1
            return mx

        ans = solve(nums, firstLen, secondLen)
        ans2 = solve(nums, secondLen, firstLen)
        return max(ans, ans2)
    