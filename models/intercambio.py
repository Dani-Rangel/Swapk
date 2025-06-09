from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean

class Intercambio(Base):
        __tablename__ = 'intercambios'
        id = Column(Integer, primary_key=True)
        ofertante_id = Column(Integer, ForeignKey('usuarios.id'))
        receptor_id = Column(Integer, ForeignKey('usuarios.id'))
        habilidad_ofrecida_id = Column(Integer, ForeignKey('habilidades.id'))
        habilidad_buscada_id = Column(Integer, ForeignKey('habilidades.id'))
        estado = Column(String(50))
        fecha_inicio = Column(DateTime)
        fecha_cierre = Column(DateTime)