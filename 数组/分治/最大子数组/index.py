from typing import List

class Solution:
    def max_sub_arr(self, arr: List[int], left: int, right: int) -> int:
        # 基本边界条件：数组只有一个元素
        if left == right:
            return arr[left]
        
        # 计算中点
        mid = (left + right) // 2
        
        # 递归求解左、右和跨中点的最大子数组和
        leftMax = self.max_sub_arr(arr, left, mid)
        rightMax = self.max_sub_arr(arr, mid + 1, right)
        crossMax = self.find_cross_max(arr, left, mid, right)
        
        # 返回三者中的最大值
        return max(leftMax, crossMax, rightMax)
        
    def find_cross_max(self, arr: List[int], left: int, mid: int, right: int) -> int:
        # 计算从中点向左的最大子数组和
        left_sum = float('-inf')
        current_sum = 0
        for i in range(mid, left - 1, -1):
            current_sum += arr[i]
            left_sum = max(left_sum, current_sum)

        # 计算从中点向右的最大子数组和
        right_sum = float('-inf')
        current_sum = 0
        for i in range(mid + 1, right + 1):
            current_sum += arr[i]
            right_sum = max(right_sum, current_sum)

        # 返回跨越中点的最大子数组和
        return left_sum + right_sum

    def test(self, nums: List[int]) -> int:
        return self.max_sub_arr(nums, 0, len(nums) - 1)

# 测试代码
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
solution = Solution()
print(solution.test(nums))  # 输出 6
