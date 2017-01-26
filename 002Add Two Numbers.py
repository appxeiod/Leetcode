# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carryover = 0
        head = []
        while l1 or l2:
            if l1:
                if l2:
                    sum = l1.val + l2.val + carryover
                    l2 = l2.next
                else:
                    sum = l1.val + carryover
                l1 = l1.next
            else:
                if l2:
                    sum = l2.val + carryover
                    l2 = l2.next
                else:
                    pass
                
            if sum >= 10:
                sum = sum - 10
                carryover = 1
            else:
                carryover = 0
            head.append(sum)
            
        if carryover == 1:
            head.append(1)
            
        return head
