from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import models.persons
import enum

class MyStatus(enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    Bloqueado = "Bloqueado"
    Suspendido = "Suspendido"
    
class User(Base):
    __tablename__ = "tbb_usuarios"

    ID = Column(Integer, primary_key=True, index=True)
    Persona_ID = Column(Integer, ForeignKey("personas.id"))
    Nombre_Usuario = Column(String(60))
    Correo_Electronico = Column(String(255))
    Contrasena = Column(LONGTEXT)
    Numero_Telefonico_Movil = Column(String(30))
    Estatus = Column(Enum(MyStatus))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    
    items = relationship("Item", back_populates="owner")