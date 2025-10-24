# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor: Initialize book details."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Called when the object is deleted."""
        # Print exactly as required: "Deleting <title>"
        print(f"Deleting {self.title}")

    def __str__(self):
        """Informal/user-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official/developer-friendly representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
