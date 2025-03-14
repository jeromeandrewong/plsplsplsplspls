"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

from heapq import heappush, heappop

"""
idea is to use a heap to make time complexity of getting next smallest number constant
1. init heap by iterating over each LL and pushing tuple containing value of head node, its index to the heap and the node itself
2. build the merged list with a dummy node as the head
3. everyime we pop from the heap, we push the node.next onto the heap
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    if not lists:
        return None

    heap = []
    for i, node in enumerate(lists):
        if node:
            heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    curr = dummy

    while heap:
        val, idx, node = heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heappush(heap, (node.next.val, idx, node.next))

    return dummy.next
