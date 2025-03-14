"""
Given a list of points in the form [[x1, y1], [x2, y2], ... [xn, yn]] and an integer , find the closest points to the origin on the 2D plane.

The distance between two points and is calculated using the formula:

√(x1 - a2)2 + (y1 - b2)2
Return the k closest points in any order.
"""

import heapq


def k_closest(points, k):
    heap = []
    for i in range(len(points)):
        x, y = points[i]
        distance = x * x + y * y

        if len(heap) < k:
            heapq.heappush(heap, (-distance, i))
        elif distance < -heap[0][0]:
            heapq.heappushpop(heap, (-distance, i))

    return [points[p[1]] for p in heap]
