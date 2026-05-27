# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = tail = ListNode()
        curr = head
        i = 1
        nums = []
        while curr and i <= right:
            if i >= left:
                nums.append(curr.val)
            else:
                tail.next = ListNode(curr.val)
                tail = tail.next
            i += 1
            curr = curr.next


        for num in nums[::-1]:
            tail.next = ListNode(num)
            tail = tail.next
        
        tail.next = curr 
    


        return dummy.next

