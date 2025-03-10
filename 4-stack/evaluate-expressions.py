def evaluate_expression(s):
    # Remove any whitespace
    s = s.replace(" ", "")

    # Add a '+' at the end to process the last number
    s += "+"

    stack = []
    current_number = 0
    last_op = "+"

    for char in s:
        # If current character is a digit, build the number
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        # Process operators
        elif char in ["+", "-", "*", "/"]:
            # Process the previous operator with the current number
            if last_op == "+":
                stack.append(current_number)
            elif last_op == "-":
                stack.append(-current_number)
            elif last_op == "*":
                stack.append(stack.pop() * current_number)
            elif last_op == "/":
                # Integer division (floor division in Python)
                stack.append(int(stack.pop() / current_number))

            # Reset for next number and store the current operator
            current_number = 0
            last_op = char

    # The final result is the sum of everything in the stack
    return sum(stack)


# Test cases
print(evaluate_expression("3+2"))  # Output: 5
print(evaluate_expression("3-19"))  # Output: -16
print(evaluate_expression("12/4*2"))  # Output: 6
print(evaluate_expression("3-5/2"))  # Output: 1
