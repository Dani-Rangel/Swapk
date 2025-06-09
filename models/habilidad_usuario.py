from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean

class HabilidadUsuario(Base):
        __tablename__ = 'habilidades_usuario'
        id = Column(Integer, primary_key=True)
        usuario_id = Column(Integer, ForeignKey('usuarios.id'))
        habilidad_id = Column(Integer, ForeignKey('habilidades.id'))
        rol = Column(String(50))
        nivel = Column(String(50))