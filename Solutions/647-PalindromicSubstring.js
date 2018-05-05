/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function (s) {
    let sArr = s.split('')
    let len = sArr.length
    let table = []
    let count = 0

    for (let i = 0; i < len; i++) {
        table[i] = new Array(len)
        for (let j = 0; j < len; j++) {
            table[i][j] = false
        }
    }
    // All substring length 1 are palindromes
    let i = 0
    while (i < len) {
        table[i][i] = true
        i++
        count++
    }
    // Check for substring length 2
    i = 0
    while (i < len - 1) {
        if (sArr[i] === sArr[i + 1]) {
            table[i][i + 1] = true
            count++
        }
        i++
    }

    // Check for substring length greater than 2
    let subLen = 3
    let k = 3
    while (k <= len) {
        i = 0
        while (i < len - k + 1) {
            // Check if substring from ith to jth index
            // if sArr[i+1] to sArr[j-1] is a palindrome
            let j = i + k - 1
            if (table[i + 1][j - 1] && sArr[i] === sArr[j]) {
                table[i][j] = true
                count++
            }
            i++
        }
        k++
    }

    return count
}
