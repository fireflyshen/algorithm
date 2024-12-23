# Problem: 15.三数之和

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 直接使用 sorted() 排序
        result = []

        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index - 1]:
                continue  # 跳过重复的元素
            left = index + 1
            right = len(nums) - 1

            while left < right:
                total = nums[index] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[index], nums[left], nums[right]])

                    # 跳过重复的元素
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 更新左右指针
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

