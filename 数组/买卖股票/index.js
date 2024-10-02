/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let max = 0,cost = Number.MAX_SAFE_INTEGER;

  for (const price of prices) {
    console.log(price);
    cost = Math.min(cost, price);
    max = Math.max(max, price - cost);
  }

  return max;
};

console.log(maxProfit([7,6,4,3,1]));