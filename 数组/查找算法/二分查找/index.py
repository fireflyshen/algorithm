
from typing import List;

class Solution:
    
    def binarySearch(self,nums:List[int],num: int) -> int:

        low = 0;
        high = len(nums) -1;
         
        while low <= high:
            mid = (low + high) // 2;
            if(nums[mid] == num):
                return mid;
            elif nums[mid] > num:
                high = mid -1
            else:
                low = mid + 1;  
        return -1

s = Solution();
print(s.binarySearch([1,2,3,4,5,6,7],7));

