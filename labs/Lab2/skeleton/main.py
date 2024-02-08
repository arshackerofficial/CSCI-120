#012345
import sys

def selection_sort(arr, ascending=True):
    """
    Perform Selection Sort on the given list.

    Parameters:
    - arr (list): The list to be sorted.
    - ascending (bool): If True, sort in ascending order; otherwise, sort in descending order.

    Returns:
    - list: The sorted list.
    """
    #WRITE YOUR CODE HERE
    
    #DO NOT WRITE ANYTHING BELOW THIS
    return arr


def main():
    # Check for the correct number of command line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py [A/D]")
        sys.exit(1)

    # Validate the command line argument
    order_arg = sys.argv[1].upper()
    if order_arg not in ['A', 'D']:
        print("Invalid argument. Use 'A' for Ascending or 'D' for Descending.")
        sys.exit(1)

    # Initialize a list of integers for testing
    original_list = [64, 25, 12, 22, 11, 5, 13, 19, 34, 32]

    # Perform the selection sort based on the command line argument
    ascending_order = True if order_arg == 'A' else False
    sorted_list = selection_sort(original_list.copy(), ascending=ascending_order)
    order = "Ascending" if ascending_order else "Descending"

    # Display the sorted list
    print(f"\nOriginal List: {original_list}")
    print(f"Sorted List ({order} Order): {sorted_list}")


if __name__ == "__main__":
    main()
