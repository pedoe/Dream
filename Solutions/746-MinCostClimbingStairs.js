var minCostClimbingStairs = function (cost) {
    let totalCost = []
    totalCost[0] = 0
    totalCost[1] = 0
    
    for(let i = 2; i <= cost.length; i++){
        totalCost[i] = Math.min(totalCost[i-1] + cost[i-1], totalCost[i-2] + cost[i-2])
    }
    
    return totalCost[cost.length]
}

