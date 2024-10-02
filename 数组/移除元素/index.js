/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function (nums, val) {
  let size = nums.length;
  for (let i = 0; i < size; i++) {
    if (nums[i] === val) {
      for (let j = i + 1; j < size; j++) {
        nums[j - 1] = nums[j];
      }
      i--;
      size--;
    }
  }

  return size;
};


