"""
Smart Library Management System
Unit 1 - Python Programming Fundamentals and Computational Thinking
Trainer Implementation Project

A simple console-based menu-driven application that allows a librarian to:
    1. Add a new book
    2. Display all books
    3. Search for a book
    4. Issue a book
    5. Return a book
    6. Exit the application
"""

# ------------------------------------------------------------------
# Global data store
# Each book is represented as a dictionary with the following keys:
#   book_id, title, author, total_copies, available_copies
# ------------------------------------------------------------------
library = []


def add_book():
    """Add a new book record to the library."""
    print("\n--- Add a New Book ---")
    book_id = input("Enter Book ID: ").strip()

    # Validation: Book ID must be unique
    for book in library:
        if book["book_id"] == book_id:
            print(f"Error: A book with ID '{book_id}' already exists.")
            return

    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()

    try:
        total_copies = int(input("Enter Total Number of Copies: ").strip())
        if total_copies <= 0:
            print("Error: Number of copies must be a positive integer.")
            return
    except ValueError:
        print("Error: Please enter a valid whole number for copies.")
        return

    new_book = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "total_copies": total_copies,
        "available_copies": total_copies,
    }
    library.append(new_book)
    print(f"Book '{title}' added successfully.")


def display_books():
    """Display all books currently stored in the library."""
    print("\n--- Library Book List ---")
    if not library:
        print("No books available in the library.")
        return

    print(f"{'ID':<8}{'Title':<25}{'Author':<20}{'Total':<8}{'Available':<10}")
    print("-" * 71)
    for book in library:
        print(f"{book['book_id']:<8}{book['title']:<25}{book['author']:<20}"
              f"{book['total_copies']:<8}{book['available_copies']:<10}")


def search_book():
    """Search for a book by Book ID or Title."""
    print("\n--- Search a Book ---")
    keyword = input("Enter Book ID or Title to search: ").strip().lower()

    results = [b for b in library
               if keyword == b["book_id"].lower() or keyword in b["title"].lower()]

    if results:
        print(f"{'ID':<8}{'Title':<25}{'Author':<20}{'Total':<8}{'Available':<10}")
        print("-" * 71)
        for book in results:
            print(f"{book['book_id']:<8}{book['title']:<25}{book['author']:<20}"
                  f"{book['total_copies']:<8}{book['available_copies']:<10}")
    else:
        print("No matching book found.")


def issue_book():
    """Issue a book to a student if a copy is available."""
    print("\n--- Issue a Book ---")
    book_id = input("Enter Book ID to issue: ").strip()

    for book in library:
        if book["book_id"] == book_id:
            if book["available_copies"] > 0:
                book["available_copies"] -= 1
                print(f"Book '{book['title']}' issued successfully. "
                      f"Available copies now: {book['available_copies']}.")
            else:
                print(f"Sorry, '{book['title']}' is currently out of stock.")
            return

    print("Error: Book ID not found.")


def return_book():
    """Return a previously issued book back to the library."""
    print("\n--- Return a Book ---")
    book_id = input("Enter Book ID to return: ").strip()

    for book in library:
        if book["book_id"] == book_id:
            if book["available_copies"] < book["total_copies"]:
                book["available_copies"] += 1
                print(f"Book '{book['title']}' returned successfully. "
                      f"Available copies now: {book['available_copies']}.")
            else:
                print("Error: All copies of this book are already in the library.")
            return

    print("Error: Book ID not found.")


def display_menu():
    """Display the main menu."""
    print("\n===== SMART LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add a New Book")
    print("2. Display All Books")
    print("3. Search a Book")
    print("4. Issue a Book")
    print("5. Return a Book")
    print("6. Exit")


def main():
    """Main program loop - the entry point of the application."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Thank you for using the Smart Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
