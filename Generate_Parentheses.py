class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # iterative method
        # lst = []
        # left, right = 0,0
        # q = [(left, right, '')]
        # while q:
        #     left, right, s = q.pop()
        #     if len(s) == 2*n:
        #         lst.append(s)
        #     if left < n:
        #         q.append((left+1, right, s+'('))
        #     if right < left:
        #         q.append((left, right+1, s+')'))

        # return (lst)
        def dfs(left, right, st):
            if len(st) == n*2:
                lst.append(st)
                return 
            if left < n:
                dfs(left+1, right, st + '(')
            if right < left:
                dfs(left, right+1, st + ')')
        lst = []
        st = ''
        dfs(0,0,st)
        return lst
        
