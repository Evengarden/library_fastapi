import bcrypt

from sqlalchemy.orm import Session
from . import schemas, models


def get_users(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.User):
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(b"user.password", salt)
    db_user = models.User(name=user.name, surname=user.surname, phone=user.phone, login=user.login,
                          password=hashed_pass, is_admin=user.is_admin)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_book(db: Session, book: schemas.Book):
    db_book = models.Book(name = book.name, category_id = book.category_id, author_fullname = book.author_fullname, date_of_create = book.date)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_user_books(db: Session, user: schemas.User):
    pass


def delete_user(db: Session, user: schemas.User):
    pass
