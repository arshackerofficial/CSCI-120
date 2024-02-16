# 815805
import sys
import math


def filter_prime_numbers(arr):
    """
    Filter prime numbers from the given list.

    Parameters:
    - arr (list): The list to be filtered.

    Returns:
    - list: The list containing only prime numbers from the original list.
    """
    prime_numbers = []
    # WRITE YOUR CODE HERE

    def is_prime(number):
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        else:
            return True

    prime_numbers = [x for x in arr if is_prime(x)]

    # DO NOT WRITE ANYTHING BELOW THIS
    return prime_numbers


def main():
    # Initialize a sorted list of integers for testing
    original_list = [2, 4, 5, 9, 10, 13, 14, 15, 17, 21]

    # Filter prime numbers from the original list
    prime_list = filter_prime_numbers(original_list.copy())

    # Display the prime numbers
    print(f"\nOriginal List: {original_list}")
    print(f"Prime Numbers: {prime_list}")


if __name__ == "__main__":
    main()
