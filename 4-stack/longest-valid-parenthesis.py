"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring. A well-formed parentheses string is one that follows these rules:

Open brackets must be closed by a matching pair in the correct order.

For example, given the string "(()", the longest valid parentheses substring is "()", which has a length of 2. Another example is the string ")()())", where the longest valid parentheses substring is "()()", which has a length of 4.
"""


def longest_valid_parentheses(s: str) -> int:
    max_len = 0
    stack = [-1]

    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        else:
            # first pop the top element
            stack.pop()
            if not stack:
                # stack is empty. update the start of the valid substring
                stack.append(i)
            else:
                # stack is not empty.
                # we can calculate the length of the valid substring
                max_len = max(max_len, i - stack[-1])

    return max_len


def test_longest_valid_parentheses():
    # Test case 1: Basic valid substring
    s1 = "(()"
    assert (
        longest_valid_parentheses(s1) == 2
    ), f"Expected 2 but got {longest_valid_parentheses(s1)}"

    # Test case 2: Multiple valid substrings
    s2 = ")()())"
    assert (
        longest_valid_parentheses(s2) == 4
    ), f"Expected 4 but got {longest_valid_parentheses(s2)}"

    # Test case 3: Empty string
    s3 = ""
    assert (
        longest_valid_parentheses(s3) == 0
    ), f"Expected 0 but got {longest_valid_parentheses(s3)}"

    # Test case 4: All invalid
    s4 = "))))"
    assert (
        longest_valid_parentheses(s4) == 0
    ), f"Expected 0 but got {longest_valid_parentheses(s4)}"

    # Test case 5: Nested valid parentheses
    s5 = "((()))"
    assert (
        longest_valid_parentheses(s5) == 6
    ), f"Expected 6 but got {longest_valid_parentheses(s5)}"

    # Test case 6: Multiple valid sections
    s6 = "()(())"
    assert (
        longest_valid_parentheses(s6) == 6
    ), f"Expected 6 but got {longest_valid_parentheses(s6)}"

    # Test case 7: Valid section with invalid parts
    s7 = "())(())"
    assert (
        longest_valid_parentheses(s7) == 4
    ), f"Expected 4 but got {longest_valid_parentheses(s7)}"

    print("All test cases passed!")


test_longest_valid_parentheses()
