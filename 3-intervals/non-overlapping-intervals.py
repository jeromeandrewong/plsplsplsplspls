"""
Write a function to return the minimum number of intervals that must be removed from a given array intervals, where intervals[i] consists of a starting point starti and an ending point endi, to ensure that the remaining intervals do not overlap.
"""

"""
this is the same as finding the number of non-overlapping intervals (total intervals - non overlapping = min number of intervals to remove)

To find the maximum number of non-overlapping intervals, we can sort the intervals by their end time. We then use a greedy approach: we iterate over each sorted interval, and repeatedly try to add that interval to the set of non-overlapping intervals. Sorting by the end time allows us to choose the intervals that end the earliest first, which frees up more time for intervals to be included later.
"""


def nonOverlappingIntervals(intervals: list[list[int]]):
    if not intervals:
        return 0

    # sort intervals by end time
    intervals.sort(key=lambda x: x[1])

    # track end time of latest interval
    end = intervals[0][1]

    # count of non-overlapping intervals (first interval always not overlapping)
    count = 1

    # start iterating from the second interval since the first interval is always not overlapping
    for i in range(1, len(intervals)):
        # if non overlap: start of curr interval after end of last interval
        if intervals[i][0] >= end:
            count += 1
            end = intervals[i][1]

    return len(intervals) - count


def test_nonOverlappingIntervals():
    # Test case 1: [[1,3],[5,8],[4,10],[11,13]]
    # Expected output: 1 (remove [4,10] to make intervals non-overlapping)
    intervals1 = [[1, 3], [5, 8], [4, 10], [11, 13]]
    assert (
        nonOverlappingIntervals(intervals1) == 1
    ), f"Expected 1 but got {nonOverlappingIntervals(intervals1)}"

    print("All test cases passed!")


test_nonOverlappingIntervals()
