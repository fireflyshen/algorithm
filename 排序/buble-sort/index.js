var bubbleSort = function (arr) {
  for (var i = arr.length; i > 0; i--) {
    let flag = false;
    for (let j = 0; j < arr.length; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        flag = true;
      }
    }
    if (!flag) break;
  }
};

let arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];

bubbleSort(arr);

console.log(arr); // [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
