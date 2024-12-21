from typing import List,Dict;

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        p:Dict[int,int] = {}
        count = 0
        for l in range(len(matrix)):
            for index,item in enumerate(matrix[l]):
                if item == 0:
                    p[count] = [l,index]
                    count+=1
                    

        # 设置0
        for i in range(len(p)):
            l,c = p.get(i)
            for i in range(len(matrix[0])):
                matrix[l][i] = 0 
            
            
            for j in range(len(matrix)):
                matrix[j][c] = 0
        
        print(matrix)
        
s = Solution()

s.setZeroes([[0, 1]])
                    
                    
        