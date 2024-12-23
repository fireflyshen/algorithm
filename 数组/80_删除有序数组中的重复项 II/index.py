# Problem: 80.删除有序数组中的重复项 II
from typing import List,Dict

class Solution:
    def _80_removeDuplicates(self, nums: List[int]) -> int:
        map: Dict[int, int] = {}
        size = len(nums)
        if not nums:
            return 0

        index = 0  # 用来指向新数组的有效位置
        for i in range(size):
            if nums[i] not in map:
                map[nums[i]] = 1
                nums[index] = nums[i]
                index += 1
            else:
                v = map.get(nums[i])
                if v < 2:  # 当前数字出现次数小于2次
                    map[nums[i]] = v + 1
                    nums[index] = nums[i]
                    index += 1

        nums[:index]
        # 返回修改后的数组长度
        return index
    
    def _80_removeDuplicatesII(self, nums: List[int]) -> int:
        if len(nums) <= 2: return len(nums)
        count = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[count - 2]:
                nums[count] = nums[i]
                count += 1
        return count

# 测试代码
s = Solution()
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
new_length = s._80_removeDuplicatesII(nums)

    