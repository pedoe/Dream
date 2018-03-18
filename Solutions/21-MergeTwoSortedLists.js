/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    let curr1 = l1
    let curr2 = l2
    let curr3 = new ListNode(0)
    let head = null
    
    head = curr3
 
    while(curr1 && curr2){
        if(curr1.val <= curr2.val){
            curr3.next = curr1
            curr1 = curr1.next
        }
        else if(curr2.val < curr1.val){
            curr3.next = curr2
            curr2 = curr2.next
        }
       	curr3 = curr3.next
    }
    
    if(!curr1) {
        curr3.next = curr2
    }
    else{
        curr3.next = curr1
    }
    
    return head.next
};
