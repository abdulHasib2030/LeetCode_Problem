class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = {}
        for i in range(len(jewels)):
            if jewels[i] not in dic:
                dic[i] = jewels[i]
        cnt = 0
        for i in range(len(stones)):
            if stones[i] in dic.values():
                cnt += 1
        return (cnt)
        