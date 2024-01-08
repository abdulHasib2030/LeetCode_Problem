class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        temp = code + code
        i, j , n = 1,0, len(code)
        if k < 0:
            i += n
        while j < n:
            if k == 0:
                ans = 0
            elif 0< k:
                ans = sum(temp[i:i+k])
            else:
                ans = sum(temp[i+k-1:i-1])
            code[j] = ans
            i += 1
            j += 1
        return code