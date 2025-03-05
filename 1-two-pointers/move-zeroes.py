"""
Given an integer array nums, write a function to rearrange the array by moving all zeros to the end while keeping the order of non-zero elements unchanged. Perform this operation in-place without creating a copy of the array.
"""


def moveZeroes(nums: list[int]):
    # Your code goes here
    nextNonZero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[nextNonZero] = nums[nextNonZero], nums[i]
            nextNonZero += 1


def test_moveZeroes():
    # Test case 1: No elements
    nums = []
    moveZeroes(nums)
    assert nums == [], "Test case 1 failed"

    # Test case 2: No zeros
    nums = [1, 2, 3]
    moveZeroes(nums)
    assert nums == [1, 2, 3], "Test case 2 failed"

    # Test case 3: All zeros
    nums = [0, 0, 0]
    moveZeroes(nums)
    assert nums == [0, 0, 0], "Test case 3 failed"

    # Test case 4: Zeros at the start
    nums = [0, 0, 1, 2, 3]
    moveZeroes(nums)
    assert nums == [1, 2, 3, 0, 0], "Test case 4 failed"

    # Test case 5: Zeros at the end
    nums = [1, 2, 3, 0, 0]
    moveZeroes(nums)
    assert nums == [1, 2, 3, 0, 0], "Test case 5 failed"

    # Test case 6: Zeros in the middle
    nums = [1, 0, 2, 0, 3]
    moveZeroes(nums)
    assert nums == [1, 2, 3, 0, 0], "Test case 6 failed"

    # Test case 7: Mixed zeros and non-zeros
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0], "Test case 7 failed"

    # Test case 8: Single element zero
    nums = [0]
    moveZeroes(nums)
    assert nums == [0], "Test case 8 failed"

    # Test case 9: Single element non-zero
    nums = [1]
    moveZeroes(nums)
    assert nums == [1], "Test case 9 failed"

    print("All test cases passed!")


# Run the test function
test_moveZeroes()
