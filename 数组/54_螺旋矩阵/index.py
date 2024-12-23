# 54. 螺旋矩阵

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        # 定义边界
        result = []
        m,n = len(matrix),len(matrix[0])
        top,bottom,left,right = 0,m-1,0,n-1
        while left <= right and top <= bottom:
            
            # 从左到右
            for col in range(left,right + 1):
                result.append(matrix[top][col])
            top = top + 1
             
            # 从上倒下
            for row in range(top,bottom + 1):
                result.append(matrix[row][right])
            right = right - 1
            
            # 从右到左
            if top <= bottom:
                for col in range(right,left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom = bottom - 1 
            
            
            # 从上到下
            if left <= right:
                for row in range(bottom,top - 1,-1):
                    result.append(matrix[row][left])
                left = left + 1 
        return result
    

