# Problem: 189.轮转数组

from typing import List;

class Solution:
    def _189_rotate(self,nums:List[int],k:int) -> None: 
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        print(nums)


s = Solution();
s._189_rotate([1,2,3,4,5,6,7],3);
