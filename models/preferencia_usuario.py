from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean

class PreferenciaUsuario(Base):
        __tablename__ = 'preferencias_usuario'
        usuario_id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
        preferencia = Column(String(100), primary_key=True)
        valor = Column(String(255))