class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i, j, cnt = 0,0,0
        n = len(s)
        substr = []
        while j < n:
            substr.append(s[j])
            if j < 2:
                j +=1
            else:
                st = set(substr)
                if len(st) == 3:
                    cnt +=1
                substr.pop(0)
                i += 1
                j += 1
        return cnt
        
