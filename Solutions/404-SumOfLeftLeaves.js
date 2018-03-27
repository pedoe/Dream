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
var sumOfLeftLeaves = function(root) {
    let ans = inOrderTraversal(root)
    return ans
};

var inOrderTraversal = function(node) {
    let sum = 0
    if(node){
        sum += inOrderTraversal(node.left)
        sum += inOrderTraversal(node.right)
        if(node.left && !node.left.left && !node.left.right){
            sum += node.left.val
        }
    }
    return sum
};
