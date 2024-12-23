# Problem: 48.旋转图像
from typing import List;

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        for i in range(n):
            for j in range(i + 1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                

        for list in range(n):
            matrix[list].reverse()
    
        print(matrix)
        
    
s = Solution()

s.rotate([[1,2,3],[4,5,6],[7,8,9]])     