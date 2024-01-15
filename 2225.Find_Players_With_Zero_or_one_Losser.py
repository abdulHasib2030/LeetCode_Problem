class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winer, loser = [], {}
        for i in matches:
            winer.append(i[0])
            if i[1] in loser:
                loser[i[1]] += 1
            else:
                loser[i[1]] = 1
        ans = []
        for i in winer:
            if i not in loser:
                ans.append(i)
        ans2 = []
        for key, value in loser.items():
            if value == 1:
                ans2.append(key)
        ans = list(set(ans))
        ans.sort()
        ans2.sort()
        result = []
        result.append(ans)
        result.append(ans2)
        return result


        