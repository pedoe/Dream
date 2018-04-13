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

// Use the inorder traverse to get all element from small number 
// to large number, then find the minimum difference
var getMinimumDifference = function(root) {
    let queue = []
    let min = null
    traverse(root, queue)    
    min = Math.abs(queue[1] - queue[0])
    for(let i = 0; i < queue.length-1; i++){
        if(Math.abs(queue[i] - queue[i+1]) < min){
            min = Math.abs(queue[i] - queue[i+1])
        }
    }

    return min
};

var traverse = function(curr, queue) {
    if(!curr){
        return
    }

    traverse(curr.left, queue)
    queue.push(curr.val)
    traverse(curr.right, queue)
} 
