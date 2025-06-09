from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean

class Habilidad(Base):
        __tablename__ = 'habilidades'
        id = Column(Integer, primary_key=True)
        nombre = Column(String(100))
        tipo = Column(String(50))
        categoria = Column(String(100))