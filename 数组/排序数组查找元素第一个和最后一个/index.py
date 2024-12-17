from typing import List;
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       
        result = [-1,-1];
        mid = self.binary_search(nums,target)
        if  mid == -1:
            return [-1,-1]

        i = j = mid
        while i >= 0:
            if i - 1 < 0:
                result[0] = i
            if(i - 1 >= 0 and nums[i - 1] != target):
                result[0] = i
                break;
            else:
                i -= 1;
        while j <= len(nums) -1:
            if j + 1 > len(nums) - 1:
                result[1] = j
                break
            
            if len(nums) > (j + 1) and nums[j + 1] != target :
                result[1] = j
                break
            else:
                j += 1
        return result;
    

    
       
    
    def binary_search(self,nums:List[int],target:int) -> int:
        l = len(nums);
        left = 0;
        right = l - 1;
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid;
            elif nums[mid] < target:
                left = mid + 1  # 目标在右半部分
            else: 
                right = mid - 1  # 目标在左半部分
        return -1;
        

s = Solution()
a = s.searchRange([2,2],2)

print(a)