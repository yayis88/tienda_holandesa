from config.database import Base
from sqlalchemy import Column, Integer, String

class Producto(Base):

  __tablename__ = "productos"

  id = Column(Integer, primary_key = True)
  title = Column(String)
  precio = Column(Integer)
  category = Column(String)
  marca = Column(String)