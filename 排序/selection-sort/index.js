/**
 * 
 * @param {number[]} nums 
 */
let selectionSort = function (nums){
    for (let i = 0; i < nums.length - 1; i++) {
        let k = i;
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[j] < nums[k]) {
                k = j;
            }
        }

        [nums[i],nums[k]] = [nums[k],nums[i]];
    }
}

// test

let nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];

selectionSort(nums);

console.log(nums); // [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
