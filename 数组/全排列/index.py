from typing import List;


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [];
        used:List[bool] = [False] * len(nums);
        currentPermutation:List[int] = [];
        self.back_track(nums,used,currentPermutation,result)
        # 回溯 
        return result;        

    def back_track(self,nums:List[int],used:List[bool],currentPermutation:List[int],result:List[List[int]]):
        if currentPermutation.__len__() == nums.__len__():
            result.append(currentPermutation[:])
            return;
        # 遍历
        for i in range(nums.__len__()):
            if used[i]:
                continue;
            currentPermutation.append(nums[i])
            used[i] = True
            self.back_track(nums, used, currentPermutation, result)

            # 撤销选择
            currentPermutation.pop()
            used[i] = False;
        return;

