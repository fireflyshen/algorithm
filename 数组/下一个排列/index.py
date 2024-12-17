# 整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。

# 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
# 整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。
# 如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

# 例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
# 类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
# 而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
# 给你一个整数数组 nums ，找出 nums 的下一个排列。

# 必须 原地 修改，只允许使用额外常数空间。

"""
示例 1：

输入：nums = [1,2,3]
输出：[1,3,2]
示例 2：

输入：nums = [3,2,1]
输出：[1,2,3]
示例 3：

输入：nums = [1,1,5]
输出：[1,5,1]


"""


from typing import List;

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = nums.__len__();
        i = n - 2;
        while i >= 0 and nums[i] >= nums[i + 1]:
            i-=1;
        if i >= 0:
            j = n - 1;
            while nums[j] <= nums[i]:
                j-=1;
            self.swap(nums,i,j);
        print(nums)
        self.reverse(nums,i+1,n-1);
        
    def swap(self, nums:List[int],x:int,y:int) -> None:
        temp = nums[x];
        nums[x] = nums[y];
        nums[y] = temp;
        
    def reverse(self,nums:List[int],start:int,end:int)->None:
        while start < end: 
            self.swap(nums,start,end);
            start+=1;
            end-=1;
        
    


s = Solution()

s.nextPermutation([1,7,7,8,9,1])

"""

## 解题思路
    1. 拿到长度
    2. 指针指向倒数第二个元素
    3. 寻找前一个值比后一个值大的，如果出现指针往左移动，就这样一直找，找到最开始的前一个值比后一个值大的📖
        `while i >= 0 and nums[i] >= nums[i + 1]:`
        比如[1,3,2,4,7,5]这个数组最终指针指向的就是3而不是7
    4. 双指针开始
        - i指向最开始的出现顺序不一致的数字，j指向数组末尾。
            - 如果j元素< i元素就说明了找到了最近的点位
                
        
        

"""