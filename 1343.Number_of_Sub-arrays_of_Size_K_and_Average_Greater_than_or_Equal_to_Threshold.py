# 

### Another Optimized Soution
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        summ = sum(arr[:k-1])
        n = len(arr)
        cnt = 0
        for i in range(n-k+1):
            summ += arr[i+k-1]
            divide = summ//k
            if divide >= threshold:
                cnt += 1
            summ -= arr[i]
        return cnt

