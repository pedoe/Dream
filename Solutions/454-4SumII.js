/**
 * @param {number[]} A
 * @param {number[]} B
 * @param {number[]} C
 * @param {number[]} D
 * @return {number}
 */

// A + B + C + D = 0 => A + B = -(C + D)
var fourSumCount = function(A, B, C, D) {
    let count = 0
    let map = {}

    for(let i = 0; i < A.length; i++){
        for(let j = 0; j < B.length; j++){
            let sum = A[i] + B[j]
            map[sum] = map[sum] ? map[sum]+1 : 1
        }
    }

    for(let i = 0; i < C.length; i++){
        for(let j = 0; j < D.length; j++){
            let sum = C[i] + D[j]
            if(map[-sum]){
                count += map[-sum]
            }
        }
    }

    return count
};

