/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
    if(!root){
        return true
    }
    
    return isSymmetricRecursion(root.left, root.right)
};

var isSymmetricRecursion = function(left, right){
    if(!left && !right){
        return true
    }
    
    if(!left || !right || left.val !== right.val){
        return false
    }
    
    return isSymmetricRecursion(left.left, right.right) && isSymmetricRecursion(left.right, right.left)
}; 
