/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {


    if (nums.length === 1 || nums.length === 0) {
        return nums;
    }

    nums.reverse();

    while(k > nums.length){
        k = k - nums.length;
    }
   
    reversePart(nums,0,k-1);
    reversePart(nums,k,nums.length -1)
    return nums;

    
};

console.log(rotate([1,2,3,4],9));


function reversePart(nums,i,j){
    
    while(i < j){
        [nums[i],nums[j]] = [nums[j],nums[i]]
        i++;
        j--;
    }

}






