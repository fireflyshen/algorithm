// 给定一个数字k，生成一个数组，比如k = 3 [1,2,3],[3,2,1],[2,1,3],[3,1,2],[2,3,1]

/**
 * @param {number} k
 */

var generatePermutations = function (k) {
  const result = [];
  const nums = Array.from({ length: k }, (_, i) => i + 1);
  /**
   *
   * 回溯:
   * 数组为2
   * 循环第一次
   * [1]
   * 递归调用，传递[1],[2]
   * [1,2]
   * 满足 path.length === k 跳出递归，结果保存
   * 执行pop将path清空
   *
   * 第二次循环指针指向1，值为2
   * 推入path [2] [1]
   * 第二次递归 [2,1] []
   * 满足 path.length === k 跳出递归，结果保存
   * 执行pop将path清空
   * @param {number[]} path
   * @param {number[]} options
   * @returns
   */

  const backtrack = (path, options) => {
    if (path.length === k) {
      result.push([...path]);
      return;
    }

    for (let i = 0; i < options.length; i++) {
      path.push(options[i]);
      backtrack(
        path,
        options.filter((_, index) => index !== i)
      );
      path.pop();
    }
  };

  backtrack([], nums);
  // return result;
  return result.sort((a, b) => {
    for (let i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) {
        return a[i] - b[i];
      }
    }
    return 0;
  });
};

/**
 * 暴力穷举
 *
 * 如果n = 3,则所有的组合必定在 000 - 999这个范围内
 * 一句这个生成所有数字，然后判断是否包含1,2,3，从而判断是否是一个合法的组合
 * @param {} n
 * @returns
 */
function generatePermutationsBruteForce(n) {
  const result = [];
  const allNumbers = Array.from({ length: n }, (_, i) => i + 1);

  // 生成所有可能的n位数
  for (let i = 0; i < Math.pow(10, n); i++) {
    let numStr = i.toString().padStart(n, "0");
    console.log(numStr);

    let numArray = numStr.split("").map(Number);

    if (isValidPermutation(numArray, allNumbers)) {
      result.push(numArray);
    }
  }

  return result.sort((a, b) => {
    for (let i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) {
        return a[i] - b[i];
      }
    }
    return 0;
  });
}



function isValidPermutation(numArray, allNumbers) {
  if (numArray.length !== allNumbers.length) return false;

  for (let num of allNumbers) {
    if (!numArray.includes(num)) return false;
  }
  return true;
}

var h = generatePermutationsBruteForce(3);

console.log(1);
