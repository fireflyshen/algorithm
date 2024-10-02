/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
  // for (let i = 0; i < nums.length; i++) {
  //     if (nums[i] >= target) {
  //         return i;
  //     }
  // }

  // return nums.length

  var left = 0;
  var right = nums.length - 1;

  while (left <= right) {
    var middle = Math.floor((left + (right - left)) / 2);
    if (nums[middle] > target) {
      right = middle - 1;
    } else if (nums[middle] < target) {
      left = middle + 1;
    } else {
      return middle;
    }
  }
  return right + 1;
};

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] >= target) {
      return i;
    }
  }

  return nums.length;
};
