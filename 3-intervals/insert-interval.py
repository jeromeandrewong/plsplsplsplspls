"""
Given a list of intervals intervals and an interval newInterval, write a function to insert newInterval into a list of existing, non-overlapping, and sorted intervals based on their starting points. The function should ensure that after the new interval is added, the list remains sorted without any overlapping intervals, merging them if needed.
"""


def insertIntervals(intervals: list[list[int]], newInterval: list[int]):
    merged = []
    i = 0
    n = len(intervals)

    # adding all intervals that end before the start of the new interval to new array
    while i < n and intervals[i][1] < newInterval[0]:
        merged.append(intervals[i])
        i += 1

    # merge all the intervals that overlap with newInterval into single interval, this involves iterating through intervals list until the current interval starts before the newInterval ends
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    merged.append(newInterval)

    # add all the intervals that start after the end of the new interval
    for j in range(i, n):
        merged.append(intervals[j])

    return merged


def test_insertIntervals():
    # Test case 1: [[1,3],[6,9]], newInterval = [2,5]
    # Expected output: [[1,5],[6,9]]
    intervals1 = [[1, 3], [6, 9]]
    newInterval1 = [2, 5]
    assert insertIntervals(intervals1, newInterval1) == [
        [1, 5],
        [6, 9],
    ], f"Expected [[1,5],[6,9]] but got {insertIntervals(intervals1, newInterval1)}"

    print("All test cases passed!")


test_insertIntervals()
