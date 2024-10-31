/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    

    // 全排列
    const res = [];
    /**
     * 
     * @param {Array} path 
     * @returns 
     */
    const bracktrace = (path) => { 
        if(path.length === nums.length) {
            res.push([...path]);
            return;
        }

        for (let i = 0; i < nums.length; i++) {
            if (path.includes(nums[i])) {
                continue;
            }
            path.push(nums[i]);
            bracktrace(path);
            path.pop(); // 撤销选择（回溯）
            
        }
     }

    bracktrace([]); 
    return res;
};



var n = permute([1,2,3]);

console.log(n);
