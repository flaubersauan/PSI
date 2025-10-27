from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine('mysql://root:FSca*2033@localhost/projeto_mvc')
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass