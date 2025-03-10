"""
Given an integer array heights representing the heights of histogram bars, write a function to find the largest rectangular area possible in a histogram, where each bar's width is 1.
"""


def largestRectangleArea(heights: list[int]):
    stack = []  # pair [start_index, height]
    max_area = 0

    # when to push to stack, and what do we push
    #   whenever next rectangle is taller. we push the start index of the last lowest rectangle
    # when to pop from stack
    #   whenever we find a rectangle that is shorter
    # we update max_area whenever we pop off the stack, and for the remaining rectangles in the stack that we haven't evaluated

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, (i - idx) * height)
            start = idx
        stack.append((start, h))

    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))

    return max_area


def test_largestRectangleArea():
    # Test case 1: Basic case
    heights1 = [2, 1, 5, 6, 2, 3]
    assert (
        largestRectangleArea(heights1) == 10
    ), f"Expected 10 but got {largestRectangleArea(heights1)}"

    # Test case 2: All same height
    heights2 = [4, 4, 4, 4]
    assert (
        largestRectangleArea(heights2) == 16
    ), f"Expected 16 but got {largestRectangleArea(heights2)}"

    # Test case 3: Ascending heights
    heights3 = [1, 2, 3, 4, 5]
    assert (
        largestRectangleArea(heights3) == 9
    ), f"Expected 9 but got {largestRectangleArea(heights3)}"

    # Test case 4: Descending heights
    heights4 = [5, 4, 3, 2, 1]
    assert (
        largestRectangleArea(heights4) == 9
    ), f"Expected 9 but got {largestRectangleArea(heights4)}"

    # Test case 5: Single bar
    heights5 = [5]
    assert (
        largestRectangleArea(heights5) == 5
    ), f"Expected 5 but got {largestRectangleArea(heights5)}"

    # Test case 6: Empty array
    heights6 = []
    assert (
        largestRectangleArea(heights6) == 0
    ), f"Expected 0 but got {largestRectangleArea(heights6)}"

    # Test case 7: Valley shape
    heights7 = [3, 1, 3]
    assert (
        largestRectangleArea(heights7) == 3
    ), f"Expected 3 but got {largestRectangleArea(heights7)}"

    print("All test cases passed!")


test_largestRectangleArea()
