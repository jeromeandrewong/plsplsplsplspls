"""
Write a function to sort a given integer array nums in-place (and without the built-in sort function), where the array contains n integers that are either 0, 1, and 2 and represent the colors red, white, and blue. Arrange the objects so that same-colored ones are adjacent, in the order of red, white, and blue (0, 1, 2).
"""


def sortColors(nums: list[int]):
    # Your code goes here
    left, right = 0, len(nums) - 1

    i = 0

    while i <= right:
        # move 0 to correct place (left pointer)
        # move 2 to correct plcae (right pointer)
        # else we just increment the position of i
        # if 0 and 2 are in the correct place, 1 will be correctly sorted in the middle

        if nums[i] == 0:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1
            i += 1

        elif nums[i] == 2:
            nums[right], nums[i] = nums[i], nums[right]
            right -= 1

        else:
            i += 1

    return nums


# Test cases
def test_sortColors():
    # Test case 1: Mixed array
    nums1 = [2, 1, 2, 0, 1, 0, 1, 0, 1]
    assert sortColors(nums1) == [0, 0, 0, 1, 1, 1, 1, 2, 2]

    # Test case 2: Already sorted array
    nums2 = [0, 0, 1, 1, 2, 2]
    assert sortColors(nums2) == [0, 0, 1, 1, 2, 2]

    # Test case 3: Reverse sorted array
    nums3 = [2, 2, 1, 1, 0, 0]
    assert sortColors(nums3) == [0, 0, 1, 1, 2, 2]

    # Test case 4: Single element array
    nums4 = [1]
    assert sortColors(nums4) == [1]

    # Test case 5: Empty array
    nums5 = []
    assert sortColors(nums5) == []

    print("All test cases passed!")


# Run tests
test_sortColors()
