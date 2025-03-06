"""
Write a function to return the length of the longest substring in a provided string s where all characters in the substring are distinct.
"""


def longestSubstringWithoutRepeat(s: str):
    # Your code goes here
    start = 0
    longest_str = 0
    seen = {}

    for end in range(len(s)):
        seen[s[end]] = seen.get(s[end], 0) + 1
        while seen[s[end]] > 1:
            seen[s[start]] -= 1
            start += 1

        longest_str = max(longest_str, end - start + 1)
    return longest_str


def test_longestSubstringWithoutRepeat():
    # Test case 1: "eghghhgg"
    # Expected output: 3 (substring "egh")
    s1 = "eghghhgg"
    assert (
        longestSubstringWithoutRepeat(s1) == 3
    ), f"Expected 3 but got {longestSubstringWithoutRepeat(s1)}"

    # Test case 2: "substring"
    # Expected output: 8 (substring "substring")
    s2 = "substring"
    assert (
        longestSubstringWithoutRepeat(s2) == 8
    ), f"Expected 8 but got {longestSubstringWithoutRepeat(s2)}"

    print("All test cases passed!")


test_longestSubstringWithoutRepeat()
