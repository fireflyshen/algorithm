// /**
//  * @param {number} n
//  * @return {number}
//  */
var tribonacci = function(n) {


    var dp = [];

    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 1;
    if (n === 0) {
        return 0
    }
    // 递推公式
    for (let i = 3; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
    }    

    return dp[dp.length -1]

    
};

// console.log(tribonacci(25))



console.log(tribonacci(25));