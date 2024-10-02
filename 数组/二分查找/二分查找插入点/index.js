/**
 * @description 二分查找插入点(无重复元素)
 * @param {number[]} arr
 * @param {number} target
 */

var binarySearchInsertionSimple = function (arr, target) {
  let i = 0;
  let j = arr.length - 1;

  while (i <= j) {
    let mid = i + Math.floor((j - i) / 2);
    if (arr[mid] < target) {
      i = mid + 1;
    } else if (arr[mid] > target) {
      j = mid - 1;
    } else {
      return mid;
    }
  }
  return i;
};

// test
// console.log(binarySearchInsertionSimple([1, 3, 6, 6, 6, 6, 6, 10, 12, 15], 6)); // 2

/**
 *
 * @param {number[]} nums
 * @param {number} target
 */
var binarySearchInsertion = function (nums, target) {
  let i = 0;
  let j = nums.length - 1;

  while (i <= j) {
    let mid = i + Math.floor((j - i) / 2);
    if (nums[mid] < target) {
      i = mid + 1;
    } else if (nums[mid] > target) {
      j = mid - 1;
    } else {
      j = mid - 1;
    }
  }


  return i;
};


// test
console.log(binarySearchInsertion([1, 3, 6, 6, 6, 6, 6, 10, 12, 15], 6)); // 2