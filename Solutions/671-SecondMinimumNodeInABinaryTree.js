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

// The binary tree should be binary search tree actually
var findSecondMinimumValue = function(root) {
    if(!root){
        return -1
    }
    let ans = [Number.MAX_VALUE]
    traverse(root, ans, root.val)
    return ans[0] === Number.MAX_VALUE ? -1 : ans[0]
    
};

var traverse = function(curr, ans, rootVal) {
    if(!curr){
        return
    } 
    if(rootVal < curr.val && curr.val < ans[0]){
        ans[0] = curr.val 
    }
    traverse(curr.left, ans, rootVal)
    traverse(curr.right, ans, rootVal)
};
