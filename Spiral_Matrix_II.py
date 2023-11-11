class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        if n == 1:
            matrix[0][0] = 1
            return (matrix)
        row, col, count = 0,0,1

        while n > 0:
            if n == 1:
                matrix[row][col] = count
                break
            for k in range(n-1):
                matrix[row][col] = count
                col += 1
                count += 1
            
            for k in range(n-1):
                matrix[row][col] = count
                row += 1
                count +=1
            
            for k in range(n -1):
                matrix[row][col] = count
                col -= 1
                count += 1
                
            for k in range(n -1):
                matrix[row][col] = count
                row -= 1
                count += 1
        
            row +=1
            col += 1
            n -= 2
        return (matrix)
            


        