"""
Write a function to find the length of the longest substring containing the same letter in a given string s, after performing at most k operations in which you can choose any character of the string and change it to any other uppercase English letter.
"""

"""
keep state of characters in window
longest repeating sequece with replacement possible is just the highest frequency character in the current window + k
"""


def characterReplacement(s: str, k: int):
    # Your code goes here
    state = {}

    res = 0
    l = 0
    highest_freq = 0

    for r in range(len(s)):
        state[s[r]] = state.get(s[r], 0) + 1
        # important to know when the window is valid
        highest_freq = max(highest_freq, state[s[r]])

        # contracting the window
        while highest_freq + k < r - l + 1:
            # decrement count of left char
            state[s[l]] -= 1
            # move left pointer
            l += 1

        res = max(res, r - l + 1)

    return res


def test_characterReplacement():
    # Test case 1: "XYYX", k=2
    # Expected output: 4 (can change both X's to Y's or both Y's to X's)
    s1 = "XYYX"
    k1 = 2
    assert (
        characterReplacement(s1, k1) == 4
    ), f"Expected 4 but got {characterReplacement(s1, k1)}"

    # Test case 2: "AAABABB", k=1
    # Expected output: 5 (can change B to A to get "AAAAA")
    s2 = "AAABABB"
    k2 = 1
    assert (
        characterReplacement(s2, k2) == 5
    ), f"Expected 5 but got {characterReplacement(s2, k2)}"

    print("All test cases passed!")


test_characterReplacement()
