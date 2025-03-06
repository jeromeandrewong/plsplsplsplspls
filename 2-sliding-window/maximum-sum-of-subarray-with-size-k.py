"""
Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.
"""


def max_subarray_sum(nums, k):
    max_sum = 0
    state = 0
    start = 0

    for end in range(len(nums)):
        state += nums[end]

        if end - start + 1 == k:
            max_sum = max(max_sum, state)
            state -= nums[start]
            start += 1

    return max_sum


def test_max_subarray_sum():
    # Test case 1: [2,1,5,1,3,2], k=3
    # Expected output: 9 (subarray [5,1,3])
    nums1 = [2, 1, 5, 1, 3, 2]
    k1 = 3
    assert (
        max_subarray_sum(nums1, k1) == 9
    ), f"Expected 9 but got {max_subarray_sum(nums1, k1)}"

    # Test case 2: [1,1,1,1,1], k=2
    # Expected output: 2 (any subarray of size 2)
    nums2 = [1, 1, 1, 1, 1]
    k2 = 2
    assert (
        max_subarray_sum(nums2, k2) == 2
    ), f"Expected 2 but got {max_subarray_sum(nums2, k2)}"

    print("All test cases passed!")


test_max_subarray_sum()
