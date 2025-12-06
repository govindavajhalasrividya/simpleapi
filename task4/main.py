from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Step 1: Create a Book model
class Book(BaseModel):
    id: int
    title: str
    author: str

# In-memory storage (our floating bookshelf)
books_db = []

# Step 2: POST - Add a new book
@app.post("/books")
def add_book(book: Book):
    books_db.append(book)
    return {"message": "Book added successfully!", "book": book}

# Step 3: GET - Get all books
@app.get("/books")
def get_books():
    return {"books": books_db}

# Step 4: GET by ID - Get a specific book
@app.get("/books/{id}")
def get_book(id: int):
    for book in books_db:
        if book.id == id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Step 5: PUT - Update a book by ID
@app.put("/books/{id}")
def update_book(id: int, updated_book: Book):
    for index, book in enumerate(books_db):
        if book.id == id:
            books_db[index] = updated_book
            return {"message": "Book updated!", "book": updated_book}
    raise HTTPException(status_code=404, detail="Book not found")

# Step 6: DELETE - Delete a book by ID
@app.delete("/books/{id}")
def delete_book(id: int):
    for index, book in enumerate(books_db):
        if book.id == id:
            deleted = books_db.pop(index)
            return {"message": "Book deleted!", "book": deleted}
    raise HTTPException(status_code=404, detail="Book not found")
