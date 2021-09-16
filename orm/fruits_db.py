# Import and call sqlalchemy functions required to write to a database file
from sqlalchemy import create_engine
engine = create_engine('sqlite:///store.db', echo=True)
from sqlalchemy.orm import declarative_base
Base = declarative_base()

# Define a class for the Fruit table, importing needed classes from SQLAlchemy
from sqlalchemy import Column, Integer, Text
class Fruit(Base):
    __tablename__ = 'fruit'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    price_cents = Column(Integer)

# Create the defined class (Fruit) as a table in the SQLite database file
Base.metadata.create_all(engine)

# Imports sqlalchemy class for creating session that connects to SQLite database
from sqlalchemy.orm import sessionmaker
# Creates a connection session with the SQLite database, so we can read and write to it
Session = sessionmaker(bind=engine)
session = Session()

# Create an apple Fruit database object and add them to the session
apple = Fruit(name='apple', price_cents=100)
session.add(apple)

# Create a pear Fruit database object and add them to the session
pear = Fruit(name='pear', price_cents=90)
session.add(pear)

# Commit the changes made in the session (this writes the new objects to the database file)
session.commit()