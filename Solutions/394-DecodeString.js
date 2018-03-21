/**
 * @param {string} s
 * @return {string}
 */

var decodeString = function(s) {
    let sArr = s.split('')
    let stack = []

    for (let i = 0; i < sArr.length; i++) {
        if (sArr[i] === ']') {
            let tempStr = []
            let tempNum = []
            let num = []
            let str = null
            let ans = ''
                // use ACII code to detemine if the number of string repeat or the string
            while (stack.length > 0 && (stack[stack.length - 1].charCodeAt(0) <= 122 &&
                    65 <= stack[stack.length - 1].charCodeAt(0))) {
                if (stack[stack.length - 1] === '[') {
                    stack.pop()
                    break
                }
                tempStr.push(stack.pop())
            }
            while (stack.length > 0 && (stack[stack.length - 1].charCodeAt(0) > 122 || 65 > stack[stack.length - 1].charCodeAt(0))) {
                tempNum.push(stack.pop())
            }
            num = parseInt(tempNum.reverse().join('')) //the left one is number of the string repeat 
            str = tempStr.reverse().join('')
            ans = ''
            for (let i = 0; i < num; i++) {
                ans += str
            }
            stack.push(ans)
        } else { 
            stack.push(sArr[i])
        }
    }
    return stack.join('')
};

console.log(decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
