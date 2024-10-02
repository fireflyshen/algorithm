/**
 *
 * @param {number} n
 */
function f(n) {
  if (n <= 0) return 0;
  if (n === 1) return 1;

  // 初始化dp数组
  let dp = [0, 1];
  // 确认递推公式
  // dp[i - 1] + dp[i - 2]
  for (let i = 2; i <= n; i++) {
      dp[i] = dp[i - 1] + dp[i - 2]
  }

  return dp[dp.length -1];
  
}

console.log(f(7))
