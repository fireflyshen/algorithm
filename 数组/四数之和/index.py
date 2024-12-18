# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
# 请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 你可以按 任意顺序 返回答案 。

 
# 示例 1：

# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# 示例 2：

# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]

from typing import List;
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 先对数组进行排序
        nums.sort()
        result = []
        n = len(nums)
    
        for i in range(n - 3):
            # 避免重复的第一个数
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                # 避免重复的第二个数
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left, right = j + 1, n - 1
                
                while left < right:
                    sum_ = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if sum_ == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # 跳过重复的数
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        # 移动双指针
                        left += 1
                        right -= 1
                    elif sum_ < target:
                        left += 1
                    else:
                        right -= 1
        
            return result
            ...
            
nums = [1, 0, -1, 0, -2, 2]
target = 0
s = Solution()
print(s.fourSum(nums, target))  
        