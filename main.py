from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db.db_config import Base, engine, SessionLocal

from db import data_access_layer, models

from db import schemas

Base.metadata.create_all(engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users", response_model=schemas.User)
def get_users(db: Session = Depends(get_db())):
    users = data_access_layer.get_users(db)
    return users


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.User, db: Session = Depends(get_db())):
    pass


@app.post("/books/", response_model=schemas.Book)
def create_books(book: schemas.Book, db: Session = Depends(get_db())):
    pass


@app.get("/user_books", response_model=models.UserBook)
def get_user_books(db: Session = Depends(get_db())):
    user_books = data_access_layer.get_user_books(db)
    return user_books


@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db())):
    pass
