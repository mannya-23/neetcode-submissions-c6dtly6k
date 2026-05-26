# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next 

        dummy = tail = ListNode()
        
        for i in range(len(nums)):
            if i == len(nums) - n:
                continue
            else:
                tail.next = ListNode(nums[i])
                tail = tail.next

        return dummy.next
