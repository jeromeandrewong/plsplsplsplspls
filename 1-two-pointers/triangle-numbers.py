"""
Write a function to count the number of triplets in an integer array nums that could form the sides of a triangle. The triplets do not need to be unique.
"""

"""
In order for a triplet to be valid lengths of a triangle, the sum of any two sides must be greater than the third side. By sorting the array, we can leverage the two-pointer technique to count all valid triplets in O(n2) time and O(1) space.
"""


def triangleNumber(nums):
    nums.sort()

    count = 0
    for i in range(len(nums) - 1, 1, -1):
        left = 0
        right = i - 1

        while left < right:
            if nums[left] + nums[right] > nums[i]:
                count += right - left
                right -= 1
            else:
                left += 1

    return count


def test_triangleNumber():
    # Test case 1: No elements
    assert triangleNumber([]) == 0, "Test case 1 failed"

    # Test case 2: One element
    assert triangleNumber([1]) == 0, "Test case 2 failed"

    # Test case 3: Two elements
    assert triangleNumber([1, 2]) == 0, "Test case 3 failed"

    # Test case 4: Three elements that cannot form a triangle
    assert triangleNumber([1, 2, 3]) == 0, "Test case 4 failed"

    # Test case 5: Three elements that can form a triangle
    assert triangleNumber([3, 4, 5]) == 1, "Test case 5 failed"

    # Test case 6: Multiple elements with multiple valid triangles
    assert triangleNumber([2, 2, 3, 4]) == 3, "Test case 6 failed"

    # Test case 7: All elements are the same
    assert triangleNumber([2, 2, 2, 2]) == 4, "Test case 7 failed"

    # Test case 8: Large numbers
    assert triangleNumber([100, 101, 102, 103, 104]) == 10, "Test case 8 failed"

    # Test case 9: Mixed numbers
    assert triangleNumber([4, 2, 3, 4]) == 4, "Test case 9 failed"

    assert triangleNumber([11, 4, 9, 6, 15, 18]) == 10, "Test case 10 passed"

    print("All test cases passed!")


# Run the test function
test_triangleNumber()
