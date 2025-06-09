from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean

class EstadisticaUsuario(Base):
        __tablename__ = 'estadisticas_usuario'
        usuario_id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
        intercambios_realizados = Column(Integer)
        reseñas_positivas = Column(Integer)
        ranking = Column(Integer)
        ultima_actividad = Column(DateTime)