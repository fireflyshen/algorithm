# 27. 移除元素

from typing import List

class Solution:
    def _27_removeElement(self, nums: List[int], val: int) -> int:
        if not nums:  # 检查是否为空
            return 0
        res = 0  # 修改初始值为 -1，这样加1后刚好指向新数组的起始位置
        for i in range(len(nums)):
            if nums[i] != val:
                nums[res] = nums[i]  # 将符合条件的元素移动到前面
                res = res + 1
        print(nums)
        return res  # 返回新数组长度

nums = [0,1,2,2,3,0,4,2]
val = 3
s = Solution()
print(s._27_removeElement(nums, val))