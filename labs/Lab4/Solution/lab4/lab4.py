# 815805
import sys


def sum_of_digits(n):
    """
    Calculate the sum of digits of a given number using recursion.

    Parameters:
    - n (int): The number for which the sum of digits needs to be calculated.

    Returns:
    - int: The sum of digits of the given number.
    """

    # WRITE YOUR CODE BELOW

    if n == 0:  # Base case
        return 0

    return n % 10 + sum_of_digits(n // 10)  # Recursive case

    # DONT WRITE ANYTHING BELOW THIS


def main():
    # Initialize an array of numbers for testing
    numbers = [123, 456, 789]

    for num in numbers:
        # Calculate the sum of digits for each number
        digit_sum = sum_of_digits(num)

        print("\nNumber is", num)

        # Display the result
        print(f"\nSum of digits of {num} is {digit_sum}.")


if __name__ == "__main__":
    main()
