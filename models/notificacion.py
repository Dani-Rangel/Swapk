from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean

class Notificacion(Base):
        __tablename__ = 'notificaciones'
        id = Column(Integer, primary_key=True)
        usuario_id = Column(Integer, ForeignKey('usuarios.id'))
        tipo = Column(String(100))
        contenido = Column(Text)
        leido = Column(Boolean, default=False)
        fecha = Column(DateTime)