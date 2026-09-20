#================================
# Working process:
#   1. We create a dummy node to serve as the starting point of the merged list and a pointer `curr` to keep track of the current position in the merged list.
#   2. We iterate through both input lists (`list1` and `list2`) simultaneously, comparing the values of the current nodes in each list.
#   3. We append the smaller value node to the merged list and move the pointer of that list to the next node.
#   4. We continue this process until we reach the end of one of the lists.
#   5. After exiting the loop, we check if there are any remaining nodes in either list. If there are, we append the remaining nodes to the merged list.   
#   6. Finally, we return the merged list starting from the node after the dummy node.
# TakeAway: Learning how to deal with nodes.
#================================


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next