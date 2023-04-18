import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, update
from sqlalchemy.orm import declarative_base, session, sessionmaker

"""Create a new database named "films_db".
Use the SQLAlchemy library to create the database and tables in Python.
Part 1: Setting up the Database
Create one table for films, with the following columns:
    films table:
        id (integer, primary key)
        title (string)
        director (string)
        release year (integer)
Part 2: Manipulating with Database
    Create script that:
        Add 3 film to the film table.
        Update 1 film
        Print data from table
        Delete all data from table"""

"""Part 1: Setting up the Database"""
engine = create_engine("sqlite:///content.db")

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Film(Base):
    __tablename__ = "films"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    release_year = Column(Integer)


Base.metadata.create_all(engine)
session.close()

"""Part 2: Setting up the Database"""

"""Add 3 film to the film table"""
Session = sessionmaker(bind=engine)
session = Session()

film1 = Film(title="John Wick 4", director="Chad Stahelski", release_year=2023)
film2 = Film(title="Lord of the Ring: The Fellowship of the Ring", director="Peter Jackson", release_year=2001)
film3 = Film(title="Lord of the Ring: The Two Towers", director="Peter Jackson", release_year=2002)

session.add(film1)
session.add(film2)
session.add(film3)

session.commit()
session.close()

"""Update 1 film"""
Session = sessionmaker(bind=engine)
session = Session()

row = session.query(Film).filter_by(id=1).first()
row.release_year = 2024
session.commit()

session.close()

"""Print data from table"""
Session = sessionmaker(bind=engine)
session = Session()

films = session.query(Film).all()
for film in films:
      print(film.id, film.title, film.director, film.release_year)

session.close()

"""Delete all data from table"""
Session = sessionmaker(bind=engine)
session = Session()

session.query(Film).delete()
session.commit()

session.close()