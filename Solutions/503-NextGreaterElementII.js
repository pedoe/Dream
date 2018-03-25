/**
 * @param {number[]} findNums
 * @param {number[]} nums
 * @return {number[]}
 */
var nextGreaterElements = function(nums) {
    let stack = []
    let ans = []
 
    for(let i = (nums.length*2)-1; i > 0; i--){
        while(stack.length > 0 && (nums[i%nums.length] >= stack[stack.length-1])){
            stack.pop()
        }
        ans[i%(nums.length)] = (stack.length === 0 ? -1 : stack[stack.length-1])
        stack.push(nums[i % nums.length])
    }
    
    return ans
};
