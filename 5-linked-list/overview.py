# basic operations


# traversing LL
def findLength(head):
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    return length


# delete given node
def deleteNode(head, target):
    if head.val == target:
        return head.next

    prev = None
    curr = head
    while curr:
        if curr.val == target:
            prev.next = curr.next
            break

        prev = curr
        curr = curr.next

    return head


# fast and slow pointers (good for cycle detection, if theres a cycle, fast pointer will eventually overlap slow pointer and they will point to the same node)
def fastAndSlow(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# reverse linked list
def reverseLinkedList(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


# Definition of a ListNode
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


# merging two sorted linked lists
def merge_lists(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next
