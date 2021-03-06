# https://leetcode.com/problems/linked-list-cycle/
# find a cycle in the linked list 

class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True