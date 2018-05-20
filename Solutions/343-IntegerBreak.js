/**
 * @param {number} n
 * @return {number}
 */

// Explanation
// https://blog.csdn.net/liyuanbhu/article/details/51198124
var integerBreak = function(n) {
    let ret = 1
    if(n === 2){
        return 1
    }
    else if(n === 3){
        return 2
    }
    else if(n === 4){
        return 4
    }
    else{
        while(n > 4){
            n -= 3
            ret *= 3
        }
    }
    
    return ret * n
};
