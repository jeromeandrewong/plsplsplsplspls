"""
Write a function to check if a person can attend all the meetings scheduled without any time conflicts. Given an array intervals, where each element [s1, e1] represents a meeting starting at time s1 and ending at time e1, determine if there are any overlapping meetings. If there is no overlap between any meetings, return true; otherwise, return false.

Note that meetings ending and starting at the same time, such as (0,5) and (5,10), do not conflict.
"""

"""
person can attend all meetings only if none overlap
if we sort meetings by start time, we can check for overlaps by comparing start time of current vs end time of previous
"""


def canAttendMeetings(intervals: list[list[int]]):
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        start_of_curr = intervals[i][0]
        end_of_prev = intervals[i - 1][1]

        if start_of_curr < end_of_prev:
            return False

    return True


def test_canAttendMeetings():
    # Test case 1: [(1,5),(3,9),(6,8)]
    # Expected output: False (meetings (1,5) and (3,9) overlap)
    intervals1 = [[1, 5], [3, 9], [6, 8]]
    assert (
        canAttendMeetings(intervals1) == False
    ), f"Expected False but got {canAttendMeetings(intervals1)}"

    # Test case 2: [(1,5),(5,10),(11,15)]
    # Expected output: True (no overlapping meetings)
    intervals2 = [[1, 5], [5, 10], [11, 15]]
    assert (
        canAttendMeetings(intervals2) == True
    ), f"Expected True but got {canAttendMeetings(intervals2)}"

    # Test case 3: [(1,5),(2,3),(4,6)]
    # Expected output: False (multiple overlapping meetings)
    intervals3 = [[1, 5], [2, 3], [4, 6]]
    assert (
        canAttendMeetings(intervals3) == False
    ), f"Expected False but got {canAttendMeetings(intervals3)}"

    print("All test cases passed!")


test_canAttendMeetings()
