"""
Write a function to find the common free time for all employees from a list called schedule. Each employee's schedule is represented by a list of non-overlapping intervals sorted by start times. The function should return a list of finite, non-zero length intervals where all employees are free, also sorted in order.
"""

"""
builds on top of merged intervals, free time of all employees is basically the gaps between their merged intervals
so we can merge all the employee meetings into a single list and find the gaps
"""


def employeeFreeTime(schedule: list[list[list[int]]]):

    # flatten schedule
    flattened = [i for employee in schedule for i in employee]
    intervals = sorted(flattened, key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged:
            merged.append(interval)

        elif interval[0] > merged[-1][1]:
            merged.append(interval)

        else:
            merged[-1][1] = max(interval[1], merged[-1][1])

    free = []

    # the free times would be the
    for j in range(1, len(merged)):
        start = merged[j - 1][1]
        end = merged[j][0]
        free.append([start, end])

    return free


def test_employeeFreeTime():
    # Test case 1: [[[2,4],[7,10]],[[1,5]],[[6,9]]]
    # Expected output: [[5,6]]
    schedule1 = [[[2, 4], [7, 10]], [[1, 5]], [[6, 9]]]
    result1 = employeeFreeTime(schedule1)
    assert result1 == [[5, 6]], f"Expected [[5,6]] but got {result1}"

    print("All test cases passed!")


test_employeeFreeTime()
