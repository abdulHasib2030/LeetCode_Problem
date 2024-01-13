from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt_s = Counter(s)
        cnt_t = Counter(t)
        diff = cnt_s - cnt_t
        return sum(diff.values())


        
        
        # n = len(s)
        # cnt = 0


        # freq = [0]*26
        # for i in range(n):
        #     freq[ord(s[i]) - ord('a')] += 1
        # for i in range(n):
        #     if freq[ord(t[i]) - ord('a')] >0:
        #         freq[ord(t[i]) - ord('a')] -= 1
        #     else:
        #         cnt += 1
        # return cnt
 


          
        
        ### Use Hash map
        # freq = {}
        # for i in range(n):
        #     if s[i] not in freq:
        #         freq[s[i]] = 1
        #     else:
        #         freq[s[i]] += 1
        # for i in range(n):
        #     if t[i] in freq and freq.get(t[i]) > 0:
        #         freq[t[i]] -=1
        #     else:
        #         cnt += 1
        # return cnt

        