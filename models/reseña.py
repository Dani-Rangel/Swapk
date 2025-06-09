from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean

class Reseña(Base):
        __tablename__ = 'reseñas'
        id = Column(Integer, primary_key=True)
        intercambio_id = Column(Integer, ForeignKey('intercambios.id'))
        autor_id = Column(Integer, ForeignKey('usuarios.id'))
        receptor_id = Column(Integer, ForeignKey('usuarios.id'))
        calificacion = Column(Integer)
        comentario = Column(Text)
        fecha = Column(DateTime)