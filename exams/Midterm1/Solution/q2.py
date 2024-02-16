#815805
def reverse_string(string):
    """
    Reverse a string without using string functions.

    Parameters:
    - string (str): The string to be reversed.

    Returns:
    - str: The reversed string.
    """
    
    reversed_string = ""
    #WRITE YOUR CODE HERE
    reversed_string = string[::-1]
    #DO NOT WRITE ANYTHING BELOW THIS
    return reversed_string

def main():
    # Default string
    orginal_string = "Hello world"

    # Reverse the default string
    reversed_str = reverse_string(orginal_string)

    # Display the original and reversed strings
    print(f"\nOriginal String: {orginal_string}")
    print(f"Reversed String: {reversed_str}")

if __name__ == "__main__":
    main()
