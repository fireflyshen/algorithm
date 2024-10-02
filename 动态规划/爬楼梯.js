
let a = 0;
/**
 * 
 * @param {*} choices 
 * @param {*} state 
 * @param {*} n 
 * @param {Map<number,number>} res
 */
function backtrack(choices, state, n, res) {
    if(state === n){
        res.set(0,res.get(0) + 1)
    }

    for (const c of choices) {
        if(state + c > n) continue;
        backtrack(choices, state + c, n, res);
        a++;
    }

}

/* 爬楼梯：回溯 */
function climbingStairsBacktrack(n) {
    const choices = [1, 2]; // 可选择向上爬 1 阶或 2 阶
    const state = 0; // 从第 0 阶开始爬
    const res = new Map();
    res.set(0, 0); // 使用 res[0] 记录方案数量
    backtrack(choices, state, n, res);
    return res.get(0);
}



console.log(climbingStairsBacktrack(3));
console.log(a);



/**
 * @param {number} n
 * @return {number}
 * 动态规划
 */
var climbStairs = function(n) {
    // 定义dp数组
    let dp = [];
    dp[0] = 1;
    dp[1] = 2;
    // 递推公式
    for (let i = 2; i < n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2]
    }

    return dp[n -1];

};

console.log(climbStairs(4));
