from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean

class Mensaje(Base):
        __tablename__ = 'mensajes'
        id = Column(Integer, primary_key=True)
        remitente_id = Column(Integer, ForeignKey('usuarios.id'))
        destinatario_id = Column(Integer, ForeignKey('usuarios.id'))
        contenido = Column(Text)
        adjunto_url = Column(String(255))
        fecha_hora = Column(DateTime)