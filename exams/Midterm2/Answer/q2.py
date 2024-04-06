# 815805
def closest_fibonacci(target):
    """
    Find the Fibonacci number closest to the given target number that is smaller than the target number,
    using recursion.

    Parameters:
    - target (int): The target number.

    Returns:
    - int: The Fibonacci number closest to the target that is smaller than the target.
    """
    # WRITE YOUR CODE BELOW 

    prev2 = 0
    prev1 = 1

    for fibo in range(target):
        newFibo = prev1 + prev2
        if newFibo >= target:
            return prev1
        prev2 = prev1
        prev1 = newFibo

    # DONT WRITE ANYTHING BELOW THIS
    pass
   

def main():
   
    input_list = [10, 30] 

    # Display the output
    for target_number in input_list:
        closest_fib = closest_fibonacci(target_number)
        print(f"\nTarget Number: {target_number}")
        print(f"Closest Fibonacci Number (Smaller than target): {closest_fib}")


if __name__ == "__main__":
    main()
