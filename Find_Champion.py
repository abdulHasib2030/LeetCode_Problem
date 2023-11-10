class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        mx = 0
        ans = 0
        for i in range(len(grid)):
          asn = sum(grid[i])
          if mx < asn:
            ans = i
          mx = max(mx, asn)

        return (ans)
        