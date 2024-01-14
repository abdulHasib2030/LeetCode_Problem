from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        lst,lst2 = [],[]
        dic, dic2 = {}, {}
        
        if len(word1) != len(word2):
            return False
        n = len(word1)
        dic = Counter(word1)
        dic2 = Counter(word2)
  
        lst = [i for i in dic.values()]
        lst2 = [i for i in dic2.values()]
        lst.sort()
        lst2.sort()

        if lst == lst2:
            for i in dic:
                if i not in dic2:
                    return False
            for i in dic2:
                if i not in dic:
                    return False
        else:
            return False
        
        return(True)

        