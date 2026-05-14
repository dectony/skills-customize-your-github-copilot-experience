from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# ----- Data model -----
class Book(BaseModel):
    id: int
    title: str
    author: str

# In-memory "database"
books: list[Book] = [
    Book(id=1, title="Python Crash Course", author="Eric Matthes"),
    Book(id=2, title="Fluent Python", author="Luciano Ramalho"),
]

# ----- Task 1: Basic GET endpoint -----
# TODO: Define a GET / route that returns a welcome message
# Example response: {"message": "Welcome to the Books API!"}


# ----- Task 2: Books collection endpoints -----
# TODO: Define a GET /books endpoint that returns all books

# TODO: Define a POST /books endpoint that accepts a Book body,
#       appends it to the list, and returns the new book


# ----- Task 3: Path & query parameters -----
# TODO: Define a GET /books/{book_id} endpoint that returns a single book
#       Return HTTP 404 with a message if the book is not found

# TODO: Add an optional `author` query parameter to GET /books
#       to filter the results by author name
