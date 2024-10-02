/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    var map = new Map()

    var size = nums.length;

    for (let i = 0; i < size; i++) {
        if(!map.has(nums[i])){
            map.set(nums[i],1);
        } else {
            var v = map.get(nums[i]);
            if (v >= 2) {
                // 移动数组，删除元素
                for (let j = i + 1 ; j < size; j++) {
                    nums[j - 1] = nums[j]
                }
                size--
                i--
            } else {
                map.set(nums[i],2)
            }
        }
    }


    nums.splice( size );
    console.log(nums);
    return size;
};


removeDuplicates([1,1,1,2,2,3])