class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        # stored sprial order array
        sprial_order = []
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # traverse for left to right 
            for col in range(left, right+1):
                sprial_order.append(matrix[top][col])
            top += 1
            # traverse for top to bottom
            for row in range(top, bottom+1):
                sprial_order.append(matrix[row][right])
            right -= 1
            if top <= bottom:
                # traverse for right to left
                for col in range(right, left-1, -1):
                    sprial_order.append(matrix[bottom][col])
                bottom -= 1
            if left <= right:
                # traverse for bottom to top
                for row in range(bottom, top-1, -1):
                    sprial_order.append(matrix[row][left])
                left += 1
        return sprial_order

ans = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(ans.spiralOrder(matrix))