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
var findBottomLeftValue = function(root) {
    let dict = {}
    traverse(root, 0, dict)
    
    return dict[Object.keys(dict).length-1][0]
};
  
var traverse = function(curr, depth, dict) {
    if(!curr){
        return 
    }
      
    let str = depth.toString()
    if(dict[str]){
       dict[str].push(curr.val)   
    }
    else{
        dict[str] = [curr.val]
    }    

    traverse(curr.left, depth+1, dict)
    traverse(curr.right, depth+1, dict)
};
