import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Author(Base):
	__tablename__ = 'author'

	id = Column(Integer, primary_key=True)
	idUser = Column(Integer, ForeignKey=True)
	FullName = Column(String(50), nullable=False)

class Article(Base):
	__tablename__ = 'articles'

	id = Column(Integer, primary_key=True)
	idAuthor = Column(Integer, ForeignKey=True)
	title = Column(String(50), nullable=False)
	body = Column(String(250), nullable=False)
	image = Column(String(250), nullable=True)
	section = Column(String(250), nullable=True)
	fecha_creacion = Column(DateTime, nullable=False)

class Comment(Base):
	__tablename__ = 'comments'

	id = Column(Integer, primary_key=True)
	idUser = Column(Integer, ForeignKey=True)
	idArticle = Column(Integer, ForeignKey=True)
	text = Column(String(50), nullable=False)
	fecha_creacion = Column(DateTime, nullable=False)

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	username = Column(String(50), nullable=False)
	email = Column(String(250), nullable=False)
	pw_hash = Column(String(250), nullable=False)

#engine = create_engine('sqlite:///blog.db')
engine = create_engine('postgresql://iuser:user@localhost/newspaper')
Base.metadata.create_all(engine)
