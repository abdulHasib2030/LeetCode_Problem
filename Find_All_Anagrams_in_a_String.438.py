class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i, j = 0,0
        lst = []
        n = len(s)
        freq1 = [0 for i in range(26) ]
        freq2 = [0 for i in range(26) ]
        for i in p:
            freq1[ord(i) - ord('a')]+= 1
        k = len(p)
        i = 0
        while j < n:
            freq2[ord(s[j]) - ord('a')] +=1
            if j < k-1:
                j += 1
            else:
                flag = True
                for v in range(26):
                    if freq1[v] != freq2[v]:
                        flag = False
                        break
                if flag:
                    lst.append(i)
                freq2[ord(s[i]) - ord('a')] -= 1
                i +=1
                j +=1

        return (lst)