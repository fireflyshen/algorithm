from typing import List;

class Solution:
    def linearSearch(self,nums:List[int],target:int)-> int:
        for item in range(len(nums)):
            if nums[item] == target:
                return item
        return -1
    
    
    
s = Solution();

t = s.linearSearch([1,23,42,34,698],42)

print(t)                