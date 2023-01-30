from fastapi import FastAPI, Form, Request, status, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional
app = FastAPI()

# @app.get("/")
# async def first_api():
#     return{"WELCOME TO FASTAPI EXAMPLE"}


class Book(BaseModel):
    id:UUID
    title:str = Field(min_length=1)
    author:str = Field(min_length=1)
    description:str
    rating: int

BOOKS = []

#Create the New books
@app.post("/")
async def create_book(book:Book):
    BOOKS.append(book)
    return book

#create book objects

def create_books_no_Api():
    book_1 = Book(id = "25559345-af76-4cb2-a989-d071a9266b57",
                  title = "GAME OF THRONES",
                  author ="DAVID",
                  description = "Fantasy",
                  rating = 100
    )
    book_2 = Book(id = "35559345-af76-4cb2-a989-d071a9266b57",
                  title = "SQUID GAMES",
                  author ="DAVID",
                  description = "THRILLER",
                  rating = 100
    )

    BOOKS.append(book_1)
    BOOKS.append(book_2)

#Get the Books
@app.get("/")
async def read_all_books():
    if len(BOOKS) < 1:
        create_books_no_Api()
    return BOOKS


#Update the BOOKS based on Book ID
@app.put("/{book_id}")
async def update_book(book_id:UUID, book:Book):
    counter = 0
    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]

#Delete the BOOK
@app.delete("/{book_id}")
async def delete_book(book_id: UUID):
    counter = 0
    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter - 1]
            return f'ID:{book_id} deleted'
    raise raise_item_be_found_exception()




#Exception Handling - Raise HTTP Exception
def raise_item_be_found_exception():
    return HTTPException(status_code=404,
                         detail= "BOOK not Found",
                         headers={"X_Header_Error": "Nothing To seen UUID"}
    )


#Get Data based on UUID
@app.get("/book{book_id}")
async def getbookbasedonuuid(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x