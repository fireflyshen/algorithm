/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
  const dp = Array(n + 1)
    .fill()
    .map(() => []);
  dp[0] = [""];

  for (let i = 1; i <= n; i++) {
    for (let j = 0; j < i; j++) {
      for (const left of dp[j]) {
        for (const right of dp[i - 1 - j]) {
          dp[i].push("(" + left + ")" + right);
        }
      }
    }
  }
  return dp[n];
};

/**
 * 动态规划
 */
var generateParenthesis2 = function (n) {
  /**
   * 明确 dp定义，dp的定义定义为每次生成括号的有效组合
   */
  const dp = Array(n + 1)
    .fill()
    .map(() => []);

  dp[0] = [""];

  /**
   * 明确递推公式
   */
  for (let i = 1; i <= n; i++) {
    for (let j = 0; j < i; j++) {
      for (const left of dp[j]) {
        for (const right of dp[i - 1 - j]) {
          dp[i].push("(" + left + ")" + right);
        }
      }
    }
  }

  console.log(dp);
};

generateParenthesis2(3);

/**
 *
 *
 * 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
 *
 * 示例 1：
 * 输入：n = 3
 * 输出：["((()))","(()())","(())()","()(())","()()()"]
 *
 * 示例 2：
 * 输入：n = 1
 * 输出：["()"]
 *
 * 提示:
 * 1 <= n <= 8
 */
