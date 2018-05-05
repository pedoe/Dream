/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if(nums.length === 0){
        return 0
    }
    else if(nums.length === 1){
        return nums[0]
    }
    
    let money = []
    money[0] = nums[0]
    money[1] = Math.max(nums[0], nums[1])

    for(let i = 2; i < nums.length; i++){
        money[i] = Math.max((money[i-2] + nums[i]), money[i-1])
    }
    
    return money[nums.length-1]
};

