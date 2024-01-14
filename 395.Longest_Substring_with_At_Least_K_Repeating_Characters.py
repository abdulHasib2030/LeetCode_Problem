class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n= len(s)
        if n < k:
            return 0
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i+1:], k)
                return max(left, right)
        return len(s)
      