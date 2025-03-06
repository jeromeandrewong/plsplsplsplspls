"""
Given an array of integers representing the value of cards, write a function to calculate the maximum score you can achieve by selecting exactly k cards from either the beginning or the end of the array.

For example, if k = 3, then you have the option to select:

the first three cards,
the last three cards,
the first card and the last two cards
the first two cards and the last card
"""

"""
need to recognise that a valid subarray of cards we can choose from is by removing n-k cards from anywhere in the middle of the array
"""


def maxScore(cards: list[int], k: int):
    total = sum(cards)
    if k >= len(cards):
        return total

    state = 0
    max_points = 0
    start = 0

    for end in range(len(cards)):
        state += cards[end]

        # the sliding window that we want to move so that we can calculate the max sum of k cards
        if end - start + 1 == len(cards) - k:
            max_points = max(max_points, total - state)
            state -= cards[start]
            start += 1

    return max_points


def test_maxScore():
    cards1 = [2, 11, 4, 5, 3, 9, 2]
    k1 = 3
    assert maxScore(cards1, k1) == 17, f"Expected 17 but got {maxScore(cards1, k1)}"

    # Test case 2: [1,1,1,1,1], k=2
    # Expected output: 2 (can pick any two cards)
    cards2 = [1, 1, 1, 1, 1]
    k2 = 2
    assert maxScore(cards2, k2) == 2, f"Expected 2 but got {maxScore(cards2, k2)}"

    # Test case 3: [1,2,3], k=3
    # Expected output: 6 (must pick all cards)
    cards3 = [1, 2, 3]
    k3 = 3
    assert maxScore(cards3, k3) == 6, f"Expected 6 but got {maxScore(cards3, k3)}"

    print("All test cases passed!")


test_maxScore()
