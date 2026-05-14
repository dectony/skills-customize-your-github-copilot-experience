# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using the FastAPI framework in Python. You will learn how to define routes, handle different HTTP methods, use path and query parameters, and model request data with Pydantic.

## 📝 Tasks

### 🛠️ Create a FastAPI App with a Basic GET Endpoint

#### Description
Set up a FastAPI application and define your first GET endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import and instantiate a `FastAPI` app
- Define a `GET /` route that returns a JSON welcome message
- Run the app using `uvicorn` so it is accessible in a browser or via `curl`

### 🛠️ Add a Books Collection with GET and POST Endpoints

#### Description
Create an in-memory list of books and expose endpoints to retrieve all books and add a new one.

#### Requirements
Completed program should:

- Store a list of book objects (each with an `id`, `title`, and `author`)
- Define a `GET /books` endpoint that returns the full list of books
- Define a `POST /books` endpoint that accepts a JSON body and adds a new book to the list
- Return the newly created book in the response

### 🛠️ Add Path Parameters and Query Parameters

#### Description
Extend the API to support retrieving a single book by ID and filtering books by author using a query parameter.

#### Requirements
Completed program should:

- Define a `GET /books/{book_id}` endpoint that returns a single book by its ID
- Return a 404 error with a descriptive message if the book is not found
- Support an optional `author` query parameter on `GET /books` to filter results by author name
