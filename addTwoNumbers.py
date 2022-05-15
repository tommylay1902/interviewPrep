# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        
        result = ListNode();
        curr = result;
        while(l1 or l2):
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            newVal = v1 + v2 + carry
            if(newVal >= 10):
                carry = 1
                curr.next = ListNode(newVal %10);
            else:
                curr.next = ListNode(newVal)
                carry = 0;
            curr = curr.next
            l1 = l1.next if l1 else None;
            l2 = l2.next if l2 else None;
        
        while l1:
            newVal = l1.val + carry
            if(newVal >= 10):
                carry = 1
                curr.next = ListNode(newVal %10);
            else:
                curr.next = ListNode(newVal)
                carry = 0;
            curr = curr.next
            l1 = l1.next
            
        while l2:
            newVal = l2.val + carry
            if(newVal >= 10):
                carry = 1
                curr.next = ListNode(newVal %10);
            else:
                curr.next = ListNode(newVal)
                carry = 0;
            curr = curr.next
            l2 = l2.next
        
        if(carry != 0):
            curr.next = ListNode(carry);
        return result.next
                