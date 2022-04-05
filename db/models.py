from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Table, Date
from sqlalchemy.orm import relationship
from db_config import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    surname = Column(String(256))
    phone = Column(String(11), nullable=True)
    login = Column(String, unique=True)
    password = Column(Text)
    is_admin = Column(Boolean, default=False)


class BookCategory(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    category_id = Column(Integer, ForeignKey('categories.id'))
    author_fullname = Column(Text)
    date_of_create = Column(Date)


user_book_table = Table('user_book', Base.metadata,
                        Column('user_id', ForeignKey('users.id')),
                        Column('book_id', ForeignKey('books.id'))
                        )
