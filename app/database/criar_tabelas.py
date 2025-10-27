from database import engine, Base
from models.user import User
from models.products import Product

Base.metadata.create_all(bind=engine)