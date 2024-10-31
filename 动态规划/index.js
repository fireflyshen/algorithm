// 给你一个整数数组 nums ，你可以对它进行一些操作。

// 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。

// 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

// 示例 1：

// 输入：nums = [3,4,2]
// 输出：6
// 解释：
// 删除 4 获得 4 个点数，因此 3 也被删除。
// 之后，删除 2 获得 2 个点数。总共获得 6 个点数。
// 示例 2：

// 输入：nums = [2,2,3,3,3,4]
// 输出：9
// 解释：
// 删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
// 之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
// 总共获得 9 个点数。

/**
 * @param {number[]} nums
 * @return {number}
 */
var deleteAndEarn = (nums) => {
  if (nums.length === 0) return 0;

  // 找出最大值
  const maxNum = Math.max(...nums);
  
  // 计算每个数字的点数总和
  const points = new Array(maxNum + 1).fill(0);
  for (const num of nums) {
    points[num] += num;
  }

  const dp = new Array(maxNum + 1).fill(0);
  dp[1] = points[1];

  for (let i = 2; i <= maxNum; i++) {
    // 递推公式
    /**
     * 假如我删除了i,那么nums[i] - 1和nums[i] + 1都必须删除，否则继续往下删除
     * 如果我不删除，那么我的最大值就是dp[i-1]，如果删除了，那么就是我删除的点数(nums[i])加上上一次我统计的最大值（dp[i-2)），
     * 因此递推公式如下
     */
    dp[i] = Math.max(dp[i - 1], dp[i - 2] + points[i]);
  }

  return dp[maxNum];
};

console.log(deleteAndEarn([1, 2, 3, 4, 99]));
