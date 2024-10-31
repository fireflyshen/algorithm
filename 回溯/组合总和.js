// // 题目：组合总和
// // 给定一个无重复的正整数数组 candidates 和一个目标整数 target，
// // 找出 candidates 中所有可以使数字和为 target 的组合。
// // 你可以任意选择 candidates 中的数字，可以重复使用同一个数字。

// 示例：

// 输入：
// candidates = [2, 3, 6, 7]
// target = 7
// 输出：
// [
//   [7],
//   [2, 2, 3]
// ]

/**
 * @param {number[]} nums
 */
var zuhe = (nums, target) => {
  let result = [];

  function backtrace(path, index) {
    var sum = path.reduce((prev, cur) => {
      return prev + cur;
    }, 0);

    if (sum === target) {
      result.push([...path]);
      return;
    }

    if (index >= nums.length || sum > target) {
      return;
    }

    path.push(nums[index]);
    backtrace(path, index);
    path.pop();
    backtrace(path, index + 1);
  }

  backtrace([], 0);
  return result;
};

var n = zuhe([2,3,6,7], 7);
console.log(n);