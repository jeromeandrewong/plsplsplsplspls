"""
Write a function to consolidate overlapping intervals within a given array intervals, where each interval intervals[i] consists of a start time starti and an end time endi. The function should return an array of the merged intervals so that no two intervals overlap and all the intervals collectively cover all the time ranges in the original input.
"""


class Solution:
    def mergeIntervals(self, intervals: list[list[int]]):
        # Your code goes here
        if not intervals:
            return []

        # sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # can always just add first interval
        merged = [intervals[0]]

        for interval in intervals:
            # if current interval has no overlap with last interval in merged
            if interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                # if theres overlap, we just overwrite the previous interval with the correct values
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


def test_mergeIntervals():
    # Test case 1: [[3,5],[1,4],[7,9],[6,8]]
    # Expected output: [[1,5],[6,9]]
    intervals1 = [[3, 5], [1, 4], [7, 9], [6, 8]]
    solution = Solution()
    result1 = solution.mergeIntervals(intervals1)
    assert result1 == [[1, 5], [6, 9]], f"Expected [[1,5],[6,9]] but got {result1}"

    # Test case 2: Empty intervals
    intervals2 = []
    result2 = solution.mergeIntervals(intervals2)
    assert result2 == [], f"Expected [] but got {result2}"

    intervals3 = [[1, 4], [4, 5]]
    result3 = solution.mergeIntervals(intervals3)
    assert result3 == [[1, 5]], f"Expected [[1,5]] but got {result3}"

    # Test case 4: Nested intervals
    intervals4 = [[1, 4], [2, 3]]
    result4 = solution.mergeIntervals(intervals4)
    assert result4 == [[1, 4]], f"Expected [[1,4]] but got {result4}"

    # Test case 5: Multiple overlapping intervals
    intervals5 = [[1, 10], [2, 6], [8, 10], [15, 18]]
    result5 = solution.mergeIntervals(intervals5)
    assert result5 == [
        [1, 10],
        [15, 18],
    ], f"Expected [[1,10],[15,18]] but got {result5}"

    # Test case 6: Overlapping intervals with earlier start time
    intervals6 = [[1, 4], [0, 2], [3, 5]]
    result6 = solution.mergeIntervals(intervals6)
    assert result6 == [[0, 5]], f"Expected [[0,5]] but got {result6}"

    # Test case 7: Large interval encompassing smaller ones
    intervals7 = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    result7 = solution.mergeIntervals(intervals7)
    assert result7 == [[1, 10]], f"Expected [[1,10]] but got {result7}"

    print("All test cases passed!")


test_mergeIntervals()
