from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from product import Base, Product


# creates data base (file) if not existed
engine = create_engine("sqlite:///products_db.sqlite", echo=True)
Base.metadata.create_all(engine)  # creates the tables for model classes

# setup things for transactions like crud operations
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
