# ------------------------------------------------------------------------------------

# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 
# 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。
# 请你返回所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。



# ------------------------------------------------------------------------------------

"""
示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。

"""


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            return [[nums[0] + nums[1] + nums[2]]] if nums[0] + nums[1] + nums[2] == 0 else [];
        sortedArr = self.sort(nums);
        result = [];

        for index in range(len(sortedArr)):
            if index > 0 and sortedArr[index] == sortedArr[index - 1]:
                continue;
            left = index + 1;
            right = len(sortedArr) -1;
            
           
            while left < right:
                sum = sortedArr[index] + sortedArr[left] + sortedArr[right];
                
                if sum == 0:
                    result.append([sortedArr[index],sortedArr[left],sortedArr[right]]);
                    while left < right and sortedArr[left] == sortedArr[left + 1]:
                        continue;
                    while left < right and sortedArr[right] == sortedArr[right - 1]:
                        continue;
                    left+=1;
                    right-=1;
                elif sum < 0:
                    left+=1;
                else:
                    right-=1;
        return result;
      

    # 快速排序，没用上😅
    def sort(self,nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums;
        # 选择基准元素
        pivot = nums[0];

        # 列表表达式，比基准小放左边，大放右边
        left = [x for x in nums[1:] if x <= pivot];
        right = [y for y in nums[1:] if y > pivot];
        
        return self.sort(left) + [pivot] + self.sort(right);