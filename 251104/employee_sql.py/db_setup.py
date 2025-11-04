from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from employee_sql import Base

# setup database
engine = create_engine('sqlite:///employees_db.sqlite',echo=True)  # create database if not exist
Base.metadata.create_all(engine)  # create the tables for model classes

# setup things for transcations (crud ops)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
