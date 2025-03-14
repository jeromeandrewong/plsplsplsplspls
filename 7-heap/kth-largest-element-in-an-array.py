"""
Write a function that takes an array of unsorted integers and an integer , and returns the kth largest element in the array. This function should run in time, where is the length of the array.
"""

import heapq


def kthLargest(nums: list[int], k: int):
    # Your code goes here
    if not nums:
        return

    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heappushpop(heap, num)

    return heap[0]
