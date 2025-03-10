"""
Given an input string s consisting solely of the characters '(', ')', ', ', '[' and ']', determine whether s is a valid string. A string is considered valid if every opening bracket is closed by a matching type of bracket and in the correct order, and every closing bracket has a corresponding opening bracket of the same type.
"""


def isValid(s: str) -> bool:
    # Your code goes here

    # think about what to add to a stack, and when to pop off the stack
    stack = []

    mapping = {
        "}": "{",
        ")": "(",
        "]": "[",
    }

    for char in s:
        if char in mapping:
            if not stack or mapping[char] != stack[-1]:
                return False
            stack.pop()

        else:
            stack.append(char)

    return len(stack) == 0


def test_isValid():
    # Test case 1: Valid parentheses
    s1 = "()"
    assert isValid(s1) == True, f"Expected True but got {isValid(s1)}"

    # Test case 2: Valid nested parentheses
    s2 = "()[]{}"
    assert isValid(s2) == True, f"Expected True but got {isValid(s2)}"

    # Test case 3: Invalid - mismatched closing bracket
    s3 = "(]"
    assert isValid(s3) == False, f"Expected False but got {isValid(s3)}"

    # Test case 4: Invalid - incorrect order
    s4 = "([)]"
    assert isValid(s4) == False, f"Expected False but got {isValid(s4)}"

    # Test case 5: Valid - complex nesting
    s5 = "{[]}"
    assert isValid(s5) == True, f"Expected True but got {isValid(s5)}"

    # Test case 6: Invalid - only opening brackets
    s6 = "((("
    assert isValid(s6) == False, f"Expected False but got {isValid(s6)}"

    # Test case 7: Invalid - only closing brackets
    s7 = ")))"
    assert isValid(s7) == False, f"Expected False but got {isValid(s7)}"

    # Test case 8: Empty string
    s8 = ""
    assert isValid(s8) == True, f"Expected True but got {isValid(s8)}"

    print("All test cases passed!")


test_isValid()
