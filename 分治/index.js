var test = function(n){

    if (n === 1) {
        return 1;
    }
    return test(n - 1) + n;
}


console.log(test(3)); // 5050