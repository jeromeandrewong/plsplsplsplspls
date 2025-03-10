"""
Given an encoded string, write a function to return its decoded string that follows a specific encoding rule: k[encoded_string], where the encoded_string within the brackets is repeated exactly k times. Note that k is always a positive integer. The input string is well-formed without any extra spaces, and square brackets are properly matched. Also, assume that the original data doesn't contain digits other than the ones that specify the number of times to repeat the following encoded_string.
"""


def decodeString(s: str):
    # think of what we want the stack to do: in this case, to keep track of nested sequences correctly
    stack = []
    # we need variable to keep track of the string that we are going to return
    string_ = ""
    # need another variable to track the number of times we are repeating a string + account for double digits
    curr_num = 0

    # while we loop through the string, there are a few actions we have to perform depending on the character we come across: "[", "]", number
    for char in s:
        if char.isdigit():
            curr_num = curr_num * 10 + int(char)
        elif char == "[":
            stack.append([string_, curr_num])
            string_ = ""
            curr_num = 0
        elif char == "]":
            prev_str, num = stack.pop()
            string_ = prev_str + num * string_
        else:
            string_ += char

    return string_


def test_decodeString():
    # Test case 1: Basic repetition
    s1 = "3[a]2[bc]"
    assert (
        decodeString(s1) == "aaabcbc"
    ), f"Expected 'aaabcbc' but got {decodeString(s1)}"

    # Test case 2: Nested brackets
    s2 = "2[3[a]b]"
    assert (
        decodeString(s2) == "aaabaaab"
    ), f"Expected 'aaabaaab' but got {decodeString(s2)}"

    # Test case 3: Multiple digits
    s3 = "10[a]"
    assert (
        decodeString(s3) == "aaaaaaaaaa"
    ), f"Expected 'aaaaaaaaaa' but got {decodeString(s3)}"

    # Test case 4: Mixed string and repetition
    s4 = "abc3[cd]xyz"
    assert (
        decodeString(s4) == "abccdcdcdxyz"
    ), f"Expected 'abccdcdcdxyz' but got {decodeString(s4)}"

    # Test case 5: Complex nesting
    s5 = "2[abc3[cd]]"
    assert (
        decodeString(s5) == "abccdcdcdabccdcdcd"
    ), f"Expected 'abccdcdcdabccdcdcd' but got {decodeString(s5)}"

    # Test case 6: Single character
    s6 = "a"
    assert decodeString(s6) == "a", f"Expected 'a' but got {decodeString(s6)}"

    # Test case 7: Empty string
    s7 = ""
    assert decodeString(s7) == "", f"Expected '' but got {decodeString(s7)}"

    print("All test cases passed!")


test_decodeString()
