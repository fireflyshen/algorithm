# --------------------------------------------------------------------------------------------

# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

# 返回这三个数的和。

# 假定每组输入只存在恰好一个解

# --------------------------------------------------------------------------------------------


"""
示例 1：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。
示例 2：

输入：nums = [0,0,0], target = 1
输出：0
解释：与 target 最接近的和是 0（0 + 0 + 0 = 0）。

"""

from typing import List,Dict;
from functools import reduce;
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:   
        
        nums.sort();
        
        result = float('inf') 
        
        if len(nums) == 3:
            # return reduce(lambda x,y: x + y, nums);
            return sum(nums);
        
        # 三个指针慢慢找
        for i in range(len(nums)):
            left = i + 1;
            right = len(nums) - 1;    
            
            if i > 0 and nums[i] == nums[i-1]: continue;
            
            
            while(left < right):
                sum = nums[i] + nums[left] + nums[right];
                
                
                if abs(sum - target) < abs(result - target):
                    result = sum;
                    
                if sum < target:
                    left+=1;
                elif sum > target:
                    right -=1;
                else:
                    return result;
                
        return result;


s  = Solution()

print(s.threeSumClosest([-1,2,1,-4],1))
                
                
                
                
                
                
        
    
