####### Built in Fuction use ##############
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
        
#         sort_S = sorted(s)
#         sort_t = sorted(t)
#         return sort_S == sort_t


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
          return False

        count_lst = [0]*26

        for i in s:
            count_lst[ord(i) - ord('a')] += 1

        for i in t:
            count_lst[ord(i) - ord('a')] -=1
            if count_lst[ord(i) - ord('a')] < 0:
               return False

        return all(i == 0 for i in count_lst)


