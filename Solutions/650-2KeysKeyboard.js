/**
 * @param {number} n
 * @return {number}
 */
var minSteps = function (n) {
    let primeArray = []
    let dp = []
    dp[0] = dp[1] = 0
    for (let i = 2; i <= n; i++) {
        if (isPrime(i)) {
            dp[i] = i
            primeArray.push(i)
        }
        else {
            for (let j = 0; j < primeArray.length; j++) {
                if (i % primeArray[j] === 0) {
                    maxDivisor = i / primeArray[j]
                    dp[i] = dp[maxDivisor] + (i / maxDivisor)
                    break
                }
            }
        }
    }
    return dp[n]
};

var isPrime = function (num) {
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) {
            return false
        }
    }
    return true
}
