# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode()
        carry = 0

        while l1 or l2 or carry:
            dig1 = l1.val if l1 else 0 
            dig2 = l2.val if l2 else 0 

            total = dig1 + dig2 + carry
            carry = total // 10
            digit = total % 10
            temp.next = ListNode(digit)
            if l1: 
                l1 = l1.next
            if l2:
                l2 = l2.next
            temp = temp.next


      
        return dummy.next