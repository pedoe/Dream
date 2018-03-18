/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let curr = head
    let reverseVal = []
    let reverse = new ListNode(0)
    let reverseCurr = reverse
    
    if(!curr){
        return null
    }
    
    while(curr){
        reverseVal.push(curr.val)
        curr = curr.next
    }
    
    for(let i = reverseVal.length-1; i >= 0 ; i--){
        reverseCurr.next = new ListNode(reverseVal[i])
        reverseCurr = reverseCurr.next
    }
    return reverse.next
};
