var insertionSort = function (arr) {

    for (let i = 1; i < arr.length; i++) {
       let base = arr[i];
       let j = i - 1;

       while(j >= 0 && arr[j] > base) {
           arr[j + 1] = arr[j];
           j--;
       }

         arr[j + 1] = base;
    }
}

let arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];

insertionSort(arr);

console.log(arr); // [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]