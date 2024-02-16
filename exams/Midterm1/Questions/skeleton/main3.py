#012345
def count_substring_occurrences(string, substring):
    """
    Count the occurrences of a substring in a given string.

    Parameters:
    - string (str): The main string to search within.
    - substring (str): The substring to count occurrences of.

    Returns:
    - int: The number of occurrences of the substring in the string.
    """
    count = 0
    #WRITE YOUR CODE HERE
    
    #DO NOT WRITE ANYTHING BELOW THIS
    return count

def main():
    # Provided string and substring
    orginal_string = "hello, hello, hello world!"
    orginal_substring = "hello"
    
    # Count occurrences of the substring in the string
    occurrences = count_substring_occurrences(orginal_string, orginal_substring)
    
    # Display the result
    print(f"Number of occurrences of '{orginal_substring}' in '{orginal_string}': {occurrences}")

if __name__ == "__main__":
    main()
