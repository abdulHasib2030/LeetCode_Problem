class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import sys
        dic, n, m, minn, cnt  = {}, len(s), len(t), sys.maxsize, 0
        if m > n:
            return ""
        for i in range(m): ## T String value or key dict add
            if t[i] in dic:
                dic[t[i]]+= 1
            else:
                dic[t[i]] = 1
                cnt += 1 
        idx1, idx2, flag = 0,0,False
        i, j = 0,0
        
        while j < n:
            if s[j] in dic: # Check j in dic
                dic[s[j]] -= 1 # dict value -1
                if dic[s[j]] == 0: # dict value 0 then cnt value -1
                    cnt -= 1
            if cnt == 0: # if all value meet then i ++
                 while cnt != 1: # condition while cnt not +
                    if s[i] in dic: # if dict thakle then dict value add 
                        dic[s[i]] += 1
                        if dic[s[i]] > 0:
                            if minn > j - i +1:
                                minn = j - i +1
                                idx1, idx2 = i, j
                                flag = True
                            cnt += 1
                    i+= 1
            j+=1

        if flag:
            return s[idx1:idx2+1]
        
        return ""



































        