/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var longestUnivaluePath = function(root) {
    if(!root){
        return 0
    }
    let max = [0]
    traverse(root, max)
    return max[0]
};

var traverse = function(curr, max) {
    if(!curr){
        return 0
    }

    let left = traverse(curr.left ? curr.left : null, max)  
    let right = traverse(curr.right ? curr.right : null, max)

    if(curr.left && curr.left.val === curr.val){
        left++
    }
    else{
        left = 0
    }

    if(curr.right && curr.right.val === curr.val){
        right++
    }
    else{
        right = 0
    }

    max[0] = max[0] < (left+right) ? (left+right) : max[0]
    return left < right ? right : left
}
