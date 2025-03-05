"""
Given an input integer array nums, write a function to find all unique triplets [nums[i], nums[j], nums[k]] such that i, j, and k are distinct indices, and the sum of nums[i], nums[j], and nums[k] equals zero. Ensure that the resulting list does not contain any duplicate triplets.
"""

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
    # helps to avoid duplicate triplets
    nums.sort()

    for i in range(len(nums)):
        # skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # init two pointers
        j = i + 1
        k = len(nums) - 1

        # two sum logic
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            # need to decrease total
            if total > 0:
                k -= 1
            # need to increase total
            elif total < 0:
                j += 1
            else:
                # found triplet, add to result list
                res.append([nums[i], nums[j], nums[k]])
                j += 1

                # skip duplicates
                while nums[j] == nums[j - 1] and j < k:
                    j += 1

    return res
