from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean

class RegistroActividad(Base):
        __tablename__ = 'registro_actividad'
        id = Column(Integer, primary_key=True)
        usuario_id = Column(Integer, ForeignKey('usuarios.id'))
        accion = Column(String(255))
        fecha_hora = Column(DateTime)