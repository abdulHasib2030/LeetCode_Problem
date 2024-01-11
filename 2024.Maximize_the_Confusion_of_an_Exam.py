class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i, n, T, F, mx= 0, len(answerKey), 0, 0, 0
        ### How many F exit answeKey string
        for j in range(n):
            if answerKey[j] == 'T':
                T+=1
            while T > k:
                if answerKey[i] == 'T':
                    T-=1
                i+=1
            mx = max(mx, (j - i) + 1)
            
        ### How many T exit answeKey string
        i = 0
        for j in range(n):
            if answerKey[j] == 'F':
                F+= 1
            while F > k:
                if answerKey[i] == 'F':
                    F-=1
                i+=1
            mx = max(mx, (j-i) +1)
        return (mx)
  
