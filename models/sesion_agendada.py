from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean

class SesionAgendada(Base):
        __tablename__ = 'sesiones_agendadas'
        id = Column(Integer, primary_key=True)
        intercambio_id = Column(Integer, ForeignKey('intercambios.id'))
        fecha_hora = Column(DateTime)
        duracion_minutos = Column(Integer)
        plataforma = Column(String(50))
        estado = Column(String(50))