/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var largestValues = function(root) {
    let d = {}
    let res = []
    if(!root){
        return []
    }

    traverse(root, 0, d)
    for(let key in d){
        let max = d[key][0]
        for(let i = 1; i < d[key].length; i++){
            if(max < d[key][i]){
                max = d[key][i]
            }
        }
        res.push(max)
    }
    return res    
};

var traverse = function(curr, depth, d) {
    if(!curr){
        return null

    }

    let key = depth.toString()
    if(d[key]){
        d[key].push(curr.val)
    }
    else{
        d[key] = [curr.val]
    }

    if(curr.left){
        traverse(curr.left, depth+1, d)
    }
    if(curr.right){
        traverse(curr.right, depth+1, d)
    }
}
