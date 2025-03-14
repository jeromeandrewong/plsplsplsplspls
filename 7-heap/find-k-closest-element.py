"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

"""

import heapq


def k_closest(nums, k, target):
    heap = []
    for num in nums:
        distance = abs(num - target)
        if len(heap) < k:
            heapq.heappush(heap, (-distance, num))
        elif distance < -heap[0][0]:
            heapq.heappushpop(heap, (-distance, num))

    distances = [pair[1] for pair in heap]
    distances.sort()
    return distances
