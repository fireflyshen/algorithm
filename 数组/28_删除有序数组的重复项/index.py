# 26. 删除有序数组中的重复项

from typing import List
class Solution:
    def _26_removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
<<<<<<< HEAD
            return 0
        res = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[res]:
                res += 1
                nums[res] = nums[i]
        return res + 1



nums = [1,1,2,2,3,3,4,4,5,5]
s = Solution()
print(s._26_removeDuplicates(nums))
=======
            return 0        
        start = 0;
        end = 1; 
        while end < len(nums):
            if nums[start] != nums[end]:
                start += 1
                nums[start] = nums[end]
            end+=1
        return start +1
>>>>>>> cec10c1f971e732acfa3b12a001135009881ad7a
