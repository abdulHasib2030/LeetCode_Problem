class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        i, j, n = 0,0, len(num)
        lst = []
        cnt = 0
        while j < n:
            lst.append(ord(num[j]) - 48)
            if j < k-1:
                j+=1
            else:
                st = ""
                for i in lst:
                    st += str(i)
                if int(st) != 0:
                    if int(num) % int(st) ==0:
                        cnt += 1
                lst.pop(0)
                i+=1
                j+= 1
        return cnt


        