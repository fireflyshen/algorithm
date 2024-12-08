from typing import List;
class Solution:
    def findSmalletIndex(self,arr:List[int]) -> int:
        smallest = arr[0]
        smallest_index = 0
        for item in range(1,len(arr),1):
            if smallest > arr[item]:
                smallest = arr[item]
                smallest_index = item
        return smallest_index
    
    def selectSort(self,arr:List[int]) -> List[int]:
        newArr=[]
        for item in range(len(arr)):
           index = self.findSmalletIndex(arr)
           newArr.append(arr.pop(index))   
        return newArr
