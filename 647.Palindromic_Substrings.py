class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        ans = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if isPalindrome(s, i, j):
                    ans += 1
        return ans
        
        