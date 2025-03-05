"""
Given an integer input array heights representing the heights of vertical lines, write a function that returns the maximum area of water that can be contained by two of the lines (and the x-axis). The function should take in an array of integers and return an integer.
"""


def max_area(heights):
    left, right = 0, len(heights) - 1
    max_area = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        curr_area = height * width

        max_area = max(max_area, curr_area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area
