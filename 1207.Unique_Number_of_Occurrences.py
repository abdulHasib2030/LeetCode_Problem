from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(Counter(arr).values())) == len(Counter(arr).values())
        # dic = {}
        # n = len(arr)
        # cnt = 0
        # for i in range(n):
        #     if arr[i] in dic:
        #         dic[arr[i]] += 1
        #     else:
        #         dic[arr[i]] = 1
        #         cnt += 1
        # st = set()
        # for i in dic.values():
        #     st.add(i)
        # if len(st) == cnt:
        #     return (True)
        # else:
        #     return (False)
        