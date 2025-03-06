"""
Given an integer array nums and an integer k, write a function to identify the highest possible sum of a subarray within nums, where the subarray meets the following criteria: its length is k, and all of its elements are unique.
"""


def maxSum(nums: list[int], k: int):
    state = {}
    max_sum = 0
    start = 0
    curr_sum = 0
    for end in range(len(nums)):
        curr_sum += nums[end]
        state[nums[end]] = state.get(nums[end], 0) + 1

        # when to move sliding window (when window is not a valid subarray)
        # 1. more than k length
        # 2. not distinct
        if end - start + 1 == k:
            if len(state) == k:
                max_sum = max(max_sum, curr_sum)

            # since not distince, we need to move the start of the sliding window and update the state
            curr_sum -= nums[start]
            state[nums[start]] -= 1
            if state[nums[start]] == 0:
                del state[nums[start]]
            start += 1

    return max_sum


def test_maxSum():
    # Test case 1: [3, 2, 2, 3, 4, 6, 7, 7, -1], k=4
    # Expected output: 20 (subarray [4, 6, 7, 3])
    nums1 = [3, 2, 2, 3, 4, 6, 7, 7, -1]
    k1 = 4
    assert maxSum(nums1, k1) == 20, f"Expected 20 but got {maxSum(nums1, k1)}"

    # Test case 2: [1, 1, 1, 1], k=2
    # Expected output: 0 (no valid subarray with distinct elements)
    nums2 = [1, 1, 1, 1]
    k2 = 2
    assert maxSum(nums2, k2) == 0, f"Expected 0 but got {maxSum(nums2, k2)}"

    # Test case 3: [1, 2, 3, 4], k=4
    # Expected output: 10 (entire array is valid)
    nums3 = [1, 2, 3, 4]
    k3 = 4
    assert maxSum(nums3, k3) == 10, f"Expected 10 but got {maxSum(nums3, k3)}"

    print("All test cases passed!")


test_maxSum()
