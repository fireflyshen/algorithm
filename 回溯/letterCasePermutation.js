/**
 * @param {String} s
 * @link https://leetcode.cn/problems/letter-case-permutation/
 * @done false 
 */



var letterCasePermutation = (s) => { 

    let STR = s.toUpperCase();

    let res = [];

    /**
     * 
     * @param {Array} path 
     */

    
    const backtrace = (path,index) => { 
        let i = 0;
        if(path.length === s.length){
            res.push(path.join(""));
            return;
        }

        if (s.length === 1 && isNaN(s)) {
            if (s.toUpperCase() == s) {
                return res.push(s,s.toLowerCase())
            } else {
                return res.push(s,s.toUpperCase())
            }
        }

        for (let i = index; i < s.length; i++) {
            var char = s[i]
            if (!isNaN(char)) {
                path.push(char);
                backtrace(path,i+1);
                path.pop()
            } else {
                path.push(char.toUpperCase());
                backtrace(path,i+1);
                path.pop();
    
                path.push(char);
                backtrace(path,i+1);
                path.pop();
            }

        
        }
       
        
    }

    backtrace([],0);
    return res;
}


var n = letterCasePermutation("ai");

console.log(n);


/////////////////////// 以上错误答案


/**
 * @param {string} s
 * @return {string[]}
 */
var letterCasePermutation = function(s) {
    const res = [];
    
    const backtrack = (path, index) => {
        if (path.length === s.length) {
            res.push(path.join(''));
            return;
        }

        const char = s[index];
        if (isNaN(char)) { // 如果是字母
            // 分支1：小写
            path.push(char.toLowerCase());
            backtrack(path, index + 1);
            path.pop();

            // 分支2：大写
            path.push(char.toUpperCase());
            backtrack(path, index + 1);
            path.pop();
        } else { // 如果是数字
            path.push(char);
            backtrack(path, index + 1);
            path.pop();
        }
    }

    backtrack([], 0);
    return res;
};

