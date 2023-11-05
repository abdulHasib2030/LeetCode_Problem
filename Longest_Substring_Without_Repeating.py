class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = set()
        cnt, mx = 0, 0
        for i in range(len(s)):
          while s[i] in k:
            k.remove(s[cnt])
            cnt += 1
          k.add(s[i])
          mx = max(i-cnt+1, mx)

        return (mx)