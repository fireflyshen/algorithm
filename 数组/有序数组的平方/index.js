/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    for (let i = 0; i < nums.length; i++) {
        nums[i] = nums[i] ** 2;
    }

    return nums.sort((a,b) =>  a-b)
};



/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    // 双指针写法
    let k = nums.length -1;
    let result = [];
    for (let i = 0 ,j = nums.length - 1; i <= j;) {
        if(nums[i] * nums[i] < nums[j] * nums[j]){
            result[k--] = nums[j] * nums[j]
            j--; 
        } else {
            result[k--] = nums[i] * nums[i];
            i++; 
        }
    }

    return result;
};

