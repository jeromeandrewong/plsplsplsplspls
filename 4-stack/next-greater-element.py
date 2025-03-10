"""
Monotonic stack qn
Given an array of integers, find the next greater element for each element in the array. The next greater element of an element x is the first element to the right of x that is greater than x. If there is no such element, then the next greater element is -1.
Example
Input: [2, 1, 3, 2, 4, 3]
Output: [3, 3, 4, 4, -1, -1]

"""

# stack will store the indexes of the elements in the input array that have not yet found their next greater element


def nextGreaterElement(nums):
    n = len(nums)
    result = [-1] * n

    stack = []

    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            # nums[i] while be the next greater element of the last element in the stack
            idx = stack.pop()
            result[idx] = nums[i]

        stack.append(i)

    return result


def test_nextGreaterElement():
    # Test case 1: Basic case
    nums1 = [2, 1, 3, 2, 4, 3]
    assert nextGreaterElement(nums1) == [
        3,
        3,
        4,
        4,
        -1,
        -1,
    ], f"Expected [3, 3, 4, 4, -1, -1] but got {nextGreaterElement(nums1)}"

    # Test case 2: All increasing
    nums2 = [1, 2, 3, 4]
    assert nextGreaterElement(nums2) == [
        2,
        3,
        4,
        -1,
    ], f"Expected [2, 3, 4, -1] but got {nextGreaterElement(nums2)}"

    # Test case 3: All decreasing
    nums3 = [4, 3, 2, 1]
    assert nextGreaterElement(nums3) == [
        -1,
        -1,
        -1,
        -1,
    ], f"Expected [-1, -1, -1, -1] but got {nextGreaterElement(nums3)}"

    # Test case 4: All equal
    nums4 = [1, 1, 1, 1]
    assert nextGreaterElement(nums4) == [
        -1,
        -1,
        -1,
        -1,
    ], f"Expected [-1, -1, -1, -1] but got {nextGreaterElement(nums4)}"

    # Test case 5: Single element
    nums5 = [5]
    assert nextGreaterElement(nums5) == [
        -1
    ], f"Expected [-1] but got {nextGreaterElement(nums5)}"

    # Test case 6: Empty array
    nums6 = []
    assert (
        nextGreaterElement(nums6) == []
    ), f"Expected [] but got {nextGreaterElement(nums6)}"

    print("All test cases passed!")


test_nextGreaterElement()
