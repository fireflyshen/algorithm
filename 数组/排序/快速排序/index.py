from typing import List;


class Solution:
    def quickSort(self,arr:List[int]) -> List[int]:
       
        if len(arr) < 2:
            return arr
        else:
            # 找出基准值
            pivot = arr[0] 
            less = [i for i in arr[1:] if pivot >= i];
            greator = [i for i in arr[1:] if pivot < i];
            return self.quickSort(less) + [pivot] + self.quickSort(greator);
    
    
    def sum(self,arr:List[int],n:int) -> int:
        
        if n == 0:
            return 0
        else:
            # 递归
            return arr[n-1] + self.sum(arr,n-1)
        
    def findMax(self,arr,left,right) -> int:
        if left == right:
            return arr[left]
        else:
            mid = (left + right) // 2
            find_left = self.findMax(arr,left,mid)
            find_right = self.findMax(arr,mid+1,right)
            print(find_left,find_right,mid)
            return max(find_left,find_right);
        
        
s=Solution();
s.test([1,2,3,4,5,6,7,8])

a = s.sum([1,2,3,4,5],5)
b= s.findMax([1,2,3,4,5,6,7],0,6)
print(b)