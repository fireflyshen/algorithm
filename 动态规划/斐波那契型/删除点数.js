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
  // 1. 找到最大值
  let max = Math.max(...nums);

  // 2. 统计次数
  let count = new Array(max + 1).fill(0);
  for (let num of nums) {
    count[num]++;
  }

  console.log(count);
  
  // 开始动态规划
  let dp = new Array(max + 1).fill(0);

  dp[0] = count[0] * 0;
  dp[1] = count[1] * 1;

  // 3. 动态规划
  /**
   * 递推公式很简单
   * 前面进行统计次数的时候可以简单的理解为，已经将数据拍好了序，
   * 这里的关键点就是理解，count数组下标就是元素，元素是之前nums数组中的元素出现的次数
   * 遍历最大值，因为之前的count数组的下标最大就是道nums数组的最大值
   * 因此这里的递推公式就是
   * dp[i] = Math.max(dp[i - 1], dp[i - 2] + count[i] * i)
   * dp中装的就是每一次选择的最大值
   * 如果选择了i，那么就无法选择i - 1 和 i + 1，因此需要计算i-1前一个数加上当前数的值 * count[i]因为出现了count[i]次
   * 
   * 
   */
  for (let i = 2; i <= max; i++) {
    dp[i] = Math.max(dp[i - 1], dp[i - 2] + count[i] * i);
  }

  return dp[max];

};

console.log(deleteAndEarn([1,2,3,2]));
/**
 * 1,2,3,4
 * 0,1,2,3,4
 */

 

