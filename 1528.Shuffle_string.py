class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = []
        for i in s:
            ans.append(i)
        for i in range(len(s)):
            ans[indices[i]] = s[i]
        res = ""
        for i in ans:
            res += i
        return (res)

