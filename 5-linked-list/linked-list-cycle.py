"""
Write a function that takes in a parameter head of type ListNode that is a reference to the head of a linked list. The function should return True if the linked list contains a cycle, and False otherwise, without modifying the linked list in any way.
"""


# Definition of a ListNode
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def hasCycle(head: ListNode) -> bool:

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def testHasCycle():
    # Test case 1: Linked list with a cycle
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Create a cycle
    assert hasCycle(node1) == True, f"Expected True but got {hasCycle(node1)}"

    # Test case 2: Linked list without a cycle
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node5.next = node6
    node6.next = node7
    assert hasCycle(node5) == False, f"Expected False but got {hasCycle(node5)}"

    # Test case 3: Empty linked list
    assert hasCycle(None) == False, f"Expected False but got {hasCycle(None)}"

    # Test case 4: Single node linked list
    node8 = ListNode(8)
    assert hasCycle(node8) == False, f"Expected False but got {hasCycle(node8)}"

    # Test case 5: Two nodes, with cycle
    node9 = ListNode(1)
    node10 = ListNode(2)
    node9.next = node10
    node10.next = node9
    assert hasCycle(node9) == True, f"Expected True but got {hasCycle(node9)}"

    # Test case 6: Two nodes, no cycle
    node11 = ListNode(1)
    node12 = ListNode(2)
    node11.next = node12
    assert hasCycle(node11) == False, f"Expected False but got {hasCycle(node11)}"

    print("All test cases passed!")


testHasCycle()
