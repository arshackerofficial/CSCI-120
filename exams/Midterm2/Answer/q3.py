# 815805
def sort_books_by_pages(books):
    """
    Sorts the list of dictionaries representing books by the number of pages in ascending order without using inbuilt function.
    use any sorting algorithm

    Parameters:
    - books (list): The list of dictionaries representing books.


    Output:
    -Print the output Here itself .Dont Return any value
    """
    # WRITE TOUR CODE BELOW    
    n = len(books)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if books[j]["pages"] < books[min_index]["pages"]:
                min_index = j
        min_value = books.pop(min_index)
        books.insert(i, min_value)
    
    print(books)

def search_book_by_title(books, title):
    
    """
    Searches for a specific book by title in the list of dictionaries representing books without using inbuilt function.
    use any searching algorithm 
    Parameters:
    - books (list): The list of dictionaries representing books.
    - title (str): The title of the book to search for.


    Output:
    -Print the output Here itself .Dont Return any value
    """
      # WRITE TOUR CODE BELOW
    for i in range(len(books)):
        book = books[i]
        if book["title"] == title:
            print(book)
    


    
def main():
    # Sample book list
    books_list = [
        {'title': 'Python Programming', 'author': 'John Doe', 'pages': 300},
        {'title': 'Introduction to Algorithms', 'author': 'Thomas Cormen', 'pages': 800},
        {'title': 'Data Structures and Algorithms in Python', 'author': 'Michael T. Goodrich', 'pages': 600},
        {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'pages': 200}
    ]

    # Sort books by number of pages
    sort_books_by_pages(books_list)

    # Search for specific books
    search_book_by_title(books_list, "Python Programming")
    search_book_by_title(books_list, "Harry Potter")

if __name__ == "__main__":
    main()
