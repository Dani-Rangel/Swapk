from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean

class Usuario(Base):
        __tablename__ = 'usuarios'
        id = Column(Integer, primary_key=True)
        nombre = Column(String(100))
        correo = Column(String(120))
        contraseña = Column(String(255))
        foto_perfil = Column(String(255))
        ubicacion = Column(String(100))
        tipo_usuario = Column(String(50))
        fecha_registro = Column(DateTime)
        estado = Column(String(20))