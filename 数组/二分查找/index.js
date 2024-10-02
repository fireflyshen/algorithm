/**
 * 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  /**
   * @type {number}
   */
  let left = 0;
  /**
   * @type {number}
   */
  let right = nums.length - 1;

  while (left <= right) {
    let middle = Math.floor((right + left) / 2); // 计算中间索引
    if (nums[middle] > target) {
      // 如果中间值大，说明值在左边，移动右边的指针
      right = middle - 1;
    } else if (nums[middle] < target) {
      // 否则移动左边的指针
      left = middle + 1;
    } else {
      // 否则返回
      return middle;
    }
  }

  return -1;
};

console.log(search([1, 2, 3, 4, 5, 6, 7, 7, 7,8, 9], 7)); // 4
