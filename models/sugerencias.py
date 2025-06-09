from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean

class Sugerencia(Base):
        __tablename__ = 'sugerencias'
        id = Column(Integer, primary_key=True)
        usuario_id = Column(Integer, ForeignKey('usuarios.id'))
        mensaje = Column(Text)
        tipo = Column(String(100))
        fecha = Column(DateTime)