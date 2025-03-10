def nextSmallerElement(nums):

    stack = []
    n = len(nums)
    result = [-1] * n

    for i in range(n):
        while stack and nums[i] < nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    return result


def test_nextSmallerElement():
    # Test case 1: Basic case
    nums1 = [2, 1, 3, 2, 4, 3]
    assert nextSmallerElement(nums1) == [
        1,
        -1,
        2,
        -1,
        3,
        -1,
    ], f"Expected [1, -1, 2, -1, 3, -1] but got {nextSmallerElement(nums1)}"

    # Test case 2: All increasing
    nums2 = [1, 2, 3, 4]
    assert nextSmallerElement(nums2) == [
        -1,
        -1,
        -1,
        -1,
    ], f"Expected [-1, -1, -1, -1] but got {nextSmallerElement(nums2)}"

    # Test case 3: All decreasing
    nums3 = [4, 3, 2, 1]
    assert nextSmallerElement(nums3) == [
        3,
        2,
        1,
        -1,
    ], f"Expected [3, 2, 1, -1] but got {nextSmallerElement(nums3)}"

    # Test case 4: All equal
    nums4 = [1, 1, 1, 1]
    assert nextSmallerElement(nums4) == [
        -1,
        -1,
        -1,
        -1,
    ], f"Expected [-1, -1, -1, -1] but got {nextSmallerElement(nums4)}"

    # Test case 5: Single element
    nums5 = [5]
    assert nextSmallerElement(nums5) == [
        -1
    ], f"Expected [-1] but got {nextSmallerElement(nums5)}"

    # Test case 6: Empty array
    nums6 = []
    assert (
        nextSmallerElement(nums6) == []
    ), f"Expected [] but got {nextSmallerElement(nums6)}"

    print("All test cases passed!")


test_nextSmallerElement()
