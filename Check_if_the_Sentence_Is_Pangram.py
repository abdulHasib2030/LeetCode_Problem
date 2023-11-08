class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        tem = ""
        for i in range(len(sentence)):
            if sentence[i] in tem:
                continue
            tem+= sentence[i]
        
        ans = 'abcdefghijklmnopqrstuvwxyz'

        te = sorted(tem)
        if len(tem) < 26:
          return (False)
        for i in range(len(te)):
          if ans[i] != te[i]:
            return (False)
        return (True)

        