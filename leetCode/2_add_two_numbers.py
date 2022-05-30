# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = l1.val + l2.val
        remainder = 1 if num > 9 else 0
        num = num % 10
        base = ListNode(num)
        l3 = base
        while l1 or l2:
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            if (not l1 and not l2 and remainder == 0):
                break
            
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            num3 = num1 + num2 + remainder
            remainder = 1 if num3 > 9 else 0
            num3 = num3 % 10
            l3.next = ListNode(num3)
            l3 = l3.next
          
        return base
        