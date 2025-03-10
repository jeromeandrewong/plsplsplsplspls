"""
Given an integer array temps representing daily temperatures, write a function to calculate the number of days one has to wait for a warmer temperature after each given day. The function should return an array answer where answer[i] represents the wait time for a warmer day after the ith day. If no warmer day is expected in the future, set answer[i] to 0.
"""


def dailyTemperatures(temps: list[int]):
    # Your code goes here
    n = len(temps)
    stack = []
    res = [0] * n

    for i in range(n):
        while stack and temps[i] > temps[stack[-1]]:
            idx = stack.pop()
            res[idx] = i - idx

        stack.append(i)

    return res


def test_dailyTemperatures():
    # Test case 1: Basic case with increasing and decreasing temperatures
    temps1 = [73, 74, 75, 71, 69, 72, 76, 73]
    assert dailyTemperatures(temps1) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ], f"Expected [1, 1, 4, 2, 1, 1, 0, 0] but got {dailyTemperatures(temps1)}"

    # Test case 2: All increasing temperatures
    temps2 = [30, 40, 50, 60]
    assert dailyTemperatures(temps2) == [
        1,
        1,
        1,
        0,
    ], f"Expected [1, 1, 1, 0] but got {dailyTemperatures(temps2)}"

    # Test case 3: All decreasing temperatures
    temps3 = [60, 50, 40, 30]
    assert dailyTemperatures(temps3) == [
        0,
        0,
        0,
        0,
    ], f"Expected [0, 0, 0, 0] but got {dailyTemperatures(temps3)}"

    # Test case 4: All equal temperatures
    temps4 = [70, 70, 70, 70]
    assert dailyTemperatures(temps4) == [
        0,
        0,
        0,
        0,
    ], f"Expected [0, 0, 0, 0] but got {dailyTemperatures(temps4)}"

    # Test case 5: Single temperature
    temps5 = [30]
    assert dailyTemperatures(temps5) == [
        0
    ], f"Expected [0] but got {dailyTemperatures(temps5)}"

    # Test case 6: Empty array
    temps6 = []
    assert (
        dailyTemperatures(temps6) == []
    ), f"Expected [] but got {dailyTemperatures(temps6)}"

    # Test case 7: Temperatures with multiple days wait
    temps7 = [70, 65, 60, 55, 80]
    assert dailyTemperatures(temps7) == [
        4,
        3,
        2,
        1,
        0,
    ], f"Expected [4, 3, 2, 1, 0] but got {dailyTemperatures(temps7)}"

    print("All test cases passed!")


test_dailyTemperatures()
