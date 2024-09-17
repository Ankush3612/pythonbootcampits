def factorial_recursive(n):
    """
    Calculates the factorial of a non-negative integer n using recursion.
    """
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

try:
    user_input = int(input("Enter a non-negative integer: "))
    if user_input < 0:
        print("Please enter a non-negative integer.")
    else:
        print(f"The factorial of {user_input} is {factorial_recursive(user_input)}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")