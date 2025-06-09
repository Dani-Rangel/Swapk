from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean

class Sesion(Base):
        __tablename__ = 'sesiones'
        id = Column(Integer, primary_key=True)
        usuario_id = Column(Integer, ForeignKey('usuarios.id'))
        token = Column(String(255))
        expira_en = Column(DateTime)