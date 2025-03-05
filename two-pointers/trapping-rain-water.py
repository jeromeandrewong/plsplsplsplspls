"""
Write a function to calculate the total amount of water trapped between bars on an elevation map, where each bar's width is 1. The input is given as an array of n non-negative integers height representing the height of each bar.
"""


def trappingWater(heights):
    if not heights:
        return 0

    count = 0
    left = 0
    right = len(heights) - 1

    left_max, right_max = heights[left], heights[right]

    while left < right:
        if right_max > left_max:
            left += 1

            if heights[left] > left_max:
                left_max = heights[left]
            else:
                count += left_max - heights[left]
        else:

            right -= 1
            if right_max < heights[right]:
                right_max = heights[right]
            else:
                count += right_max - heights[right]

    return count


def test_trappingWater():
    # Test case 1: Example case
    height = [3, 4, 1, 2, 2, 5, 1, 0, 2]
    assert trappingWater(height) == 10, "Test case 1 failed"

    # Test case 2: Empty array
    assert trappingWater([]) == 0, "Test case 2 failed"

    # Test case 3: Single element
    assert trappingWater([5]) == 0, "Test case 3 failed"

    # Test case 4: No water can be trapped
    assert trappingWater([1, 2, 3, 4, 5]) == 0, "Test case 4 failed"

    # Test case 5: Simple valley
    assert trappingWater([3, 1, 3]) == 2, "Test case 5 failed"

    # Test case 6: Multiple valleys
    assert trappingWater([3, 0, 2, 0, 4]) == 7, "Test case 6 failed"

    # Test case 7: All same height
    assert trappingWater([2, 2, 2, 2]) == 0, "Test case 7 failed"

    print("All test cases passed!")


# Run tests
test_trappingWater()
