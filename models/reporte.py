from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean

class Reporte(Base):
        __tablename__ = 'reportes'
        id = Column(Integer, primary_key=True)
        reportado_id = Column(Integer, ForeignKey('usuarios.id'))
        reportador_id = Column(Integer, ForeignKey('usuarios.id'))
        motivo = Column(String(255))
        detalle = Column(Text)
        estado = Column(String(50))
        fecha = Column(DateTime)