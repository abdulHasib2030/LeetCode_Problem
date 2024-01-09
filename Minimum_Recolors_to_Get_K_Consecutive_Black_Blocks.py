import sys
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i, j, n, cnt = 0,0,len(blocks), 0
        minn = sys.maxsize
        while j < n:
            if blocks[j] == 'W':
                cnt += 1
            if j < k-1:
                j+= 1
            else:
                minn = min(minn, cnt)
                if blocks[i] == 'W':
                    cnt -= 1
                i+= 1
                j+=1
        return minn


        