class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(grid)):
          for j in range(len(grid[i])):
            ans.append(grid[i][j])
        ans.sort()
        dic = {}
        res = []

        for i in ans:
          if i in dic:
            dic[i] += 1
            res.append(i)
          else:
            dic[i] = 1


        for i in range(len(ans)):
          if i +1 not in dic.keys():
            res.append(i+1)

        return (res)
